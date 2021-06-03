import pandas as pd

df=pd.read_csv("country_vaccination_stats.csv")
df=df.fillna(value=0)
print(df)
