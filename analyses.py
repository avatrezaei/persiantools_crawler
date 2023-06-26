import pandas as pd

# Load your data into a pandas DataFrame
df = pd.read_csv('output.csv')

# Find the 10 most viewed topics
most_viewed = df.sort_values('Views', ascending=False).head(10)

# Find the 10 most replied to topics
most_replied = df.sort_values('Replies', ascending=False).head(10)

# Find the correlation between views and replies
correlation = df['Views'].corr(df['Replies'])

print("10 most viewed topics:")
print(most_viewed)

print("\n10 most replied to topics:")
print(most_replied)

print("\nCorrelation between views and replies:", correlation)

import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('output.csv')

# Convert Replies and Views to int for analysis
df['Replies'] = df['Replies']
df['Views'] = df['Views']

# Top 10 topics by number of replies
top_replies = df.sort_values('Replies', ascending=False).head(10)

# Top 10 topics by number of views
top_views = df.sort_values('Views', ascending=False).head(10)

# Plotting the data
fig, ax = plt.subplots(2, 1, figsize=(10, 10))

top_replies.plot(kind='bar', x='Topic Title', y='Replies', ax=ax[0])
ax[0].set_title('Top 10 Topics by Replies')

top_views.plot(kind='bar', x='Topic Title', y='Views', ax=ax[1])
ax[1].set_title('Top 10 Topics by Views')

plt.tight_layout()
plt.show()