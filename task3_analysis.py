import pandas as pd
import numpy as np

# 1 — Load and Explore (4 marks)
# Load data/trends_clean.csv into a Pandas DataFrame
df = pd.read_csv("/content/data/trends_clean.csv")

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

