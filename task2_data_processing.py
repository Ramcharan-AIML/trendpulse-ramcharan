# Q: 2
# TASK_2 — Clean the Data & Save as CSV

import pandas as pd
import json
import numpy as np
import os

with open('/content/trends_260402.json' , 'r') as file:
    data = json.load(file)

df = pd.DataFrame(data)
df

# 1 — Load the JSON File (4 marks)

print(df.shape)
print(f'Loaded {len(df)} stories from trends_260402.json')

# ------------------------------------------------------------------
# 2 — Clean the Data (10 marks)

# Duplicates — remove any rows with the same post_id
df.duplicated(subset=['post_id']).sum()

# there is 0 duplicates, so no need to remove it 
print(f'\nAfter removing duplicates: {len(df)}')

# Missing values — drop rows where post_id, title, or score is missing
df.isnull().sum()

# there are o nulls in the data ,no need to remove it
print(f'After removing nulls: {len(df)}')


# Data types — make sure score and num_comments are integers
df['score'].dtype
df['num_comments'].dtype
#The score and num_comments are integer type only , no need to do any datatype changes



# Low quality — remove stories where score is less than 5
df.drop(df[df["score"] < 5].index, inplace=True)
print(f'After removing nulls: {len(df)}')

# Whitespace — strip extra spaces from the title column
df['title'] = df['title'].str.strip()


