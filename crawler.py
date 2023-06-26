import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://forum.persiantools.com"
base_url = "https://forum.persiantools.com/forums/%D9%88%DB%8C%DA%98%D9%87-%DA%A9%D8%A7%D8%B1%D8%A8%D8%B1%D8%A7%D9%86-%D8%B9%D9%85%D9%88%D9%85%DB%8C.79/page-"
total_pages = 5


def convert_to_number(num_str):
    try:
        if num_str[-1] == 'K':
            return int(float(num_str[:-1]) * 1000)
        elif num_str[-1] == 'M':
            return int(float(num_str[:-1]) * 1000000)
        else:
            return int(num_str)
    except ValueError:
        return 0  # Return 0 if the string cannot be converted to an integer


def get_data(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    topics = soup.find_all('div', class_='structItem')
    data = []
    for topic in topics:
        topic_container = topic.find('div', class_='structItem-title')
        if topic_container is not None:
            topic_title = topic_container.text.strip()
            link = topic_container.find('a').get('href')

            link = url + link if 'http' not in link else link  # Check if the link is relative or absolute
            
            meta = topic.find('div', class_='structItem-cell structItem-cell--meta')
            if meta:
                replies = meta.find('dd').text.strip().replace(',', '') if meta.find('dd') else '0'
                views = meta.find_all('dd')[1].text.strip().replace(',', '') if len(meta.find_all('dd')) > 1 else '0'
                replies = convert_to_number(replies) 
                views = convert_to_number(views)
            else:
                replies = 0
                views = 0

            data.append([topic_title, link, replies, views])
    return data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Topic Title", "Link", "Replies", "Views"])
        writer.writerows(data)

   

# Scrape data from each page and save it to the CSV file
all_data = []
for page_number in range(1, total_pages + 1):
    page_url = base_url + str(page_number)
    data = get_data(page_url)
    all_data.extend(data)  # Combine data from all pages

# Sort the data based on the number of replies (in descending order)
all_data.sort(key=lambda x: x[2], reverse=True)  

# Now save sorted data to csv
save_to_csv(all_data, 'output.csv')
