import json
import pandas as pd
import numpy as np

with open('data/trends_260402.json' , 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

print(df)
print(df.shape)
print(df.duplicated().sum())