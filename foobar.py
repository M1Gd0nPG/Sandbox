#!/usr/local/bin/python3

import pandas as pd
df = pd.read_csv('addtitle.csv')

df = df[["project" , "title", "members", "role"]]
print(df.head(3))

Final = df['role'].groupby([df.project, df.members]).apply(list).reset_index()
print(Final.head(3))
Final.to_csv("Final.csv", index=False)
