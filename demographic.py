import pandas as pd
import numpy as np

df = pd.read_csv('articles.csv')

df = df.sort_values('eventScore', ascending=False)

output = df[['title', 'url', 'lang','text']].head(20).values.tolist()
