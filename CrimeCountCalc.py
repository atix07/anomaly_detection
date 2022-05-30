import pandas as pd

df = pd.read_csv('crime.csv', encoding='windows-1252')

df['OCCURRED_ON_DATE'] = pd.to_datetime(df['OCCURRED_ON_DATE'], dayfirst=True)

df1 = df['OCCURRED_ON_DATE'].dt.date.value_counts().sort_index().reset_index()
df1.columns = ['DATE','Count']
df1.to_csv('Output.csv', index = False)