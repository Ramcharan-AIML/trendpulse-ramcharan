# Task 3 — Analysis with Pandas & NumPy

import pandas as pd
import numpy as np

# 1 — Load and Explore (4 marks)
# Load data/trends_clean.csv into a Pandas DataFrame
df = pd.read_csv("data/trends_clean.csv")

# Print the first 5 rows
print(df.head(5))

# Print the shape of the DataFrame (rows and columns)
print(f"\nLoaded data : {df.shape}")

# Print the average score and average num_comments across all stories
avg_score = df['score'].mean()
avg_comments = df['num_comments'].mean()
print(f'\nAverage score : {avg_score}')
print(f'Average Comments : {round(avg_comments,2)}')

# ----------------------------------------------------------------------------

# 2 — Basic Analysis with NumPy (8 marks)
# Use NumPy to answer these questions and print the results:
# What is the mean, median, and standard deviation of score?
mean_score = np.mean(df['score'])
median_score = np.median(df['score'])
std_score = np.std(df['score'])

print(f'\nMean score : {mean_score}')
print(f'Median score : {median_score}')
print(f'Std deviation : {round(std_score,2)}')

# What is the highest score and lowest score?
max_score = np.max(df['score'])
min_score = np.min(df['score'])

print(f'\nMax score : {max_score}')
print(f'Min score : {min_score}')

# Which category has the most stories?
most_stories = df['subreddit'].value_counts().idxmax()
max_value = df['subreddit'].value_counts().max()

print(f'Most stories in : {most_stories} {max_value} stories')

# Which story has the most comments? Print its title and comment count.
most_commented_story = df.groupby('title')['num_comments'].max().sort_values(ascending=False).idxmax()
most_commented_story_value = df.groupby('title')['num_comments'].max().max()

print(f"Most commented story : {most_commented_story} - {most_commented_story_value} comments")

# ---------------------------------------------------------------------------------

# 3 — Add New Columns (5 marks)
# Add these two new columns to your DataFrame:

# Column  Formula
# engagement  num_comments / (score + 1) — how much discussion a story gets per upvote
# is_popular  True if score > average score, else False
df['engagement'] = (df['num_comments'] / (df['score'] + 1))
df['is_popular'] = np.where(df['score'] > df['score'].mean() , True , False)
df

# -----------------------------------------------------------------------------------

# 4 — Save the Result (3 marks)
# Save the updated DataFrame (with the 2 new columns) to data/trends_analysed.csv

# os.makedirs("data" , exist_ok=True)

df.to_csv("data/trends_analysed.csv", index=False)

# Print a confirmation message
print("Saved to data/trends_analysed.csv")