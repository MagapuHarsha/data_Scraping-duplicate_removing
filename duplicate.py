import pandas as pd
pd.set_option('display.max_rows',2800)
pd.set_option('display.max_columns',10)
df = pd.read_csv('eco_friendly_labeled.csv')
df[~df.duplicated(subset=['name'])].to_csv('list(clean).csv')