import pandas as pd

df=pd.read_csv("country_vaccination_stats.csv")
df=df.fillna(value=0)

liste=df["country"].unique()
liste=list(liste)

df.index=df["country"]

df.drop("country",axis=1,inplace=True)

liste2=[]
liste3=[]

for i in liste:
    name=i
    x=df.loc[i]["daily_vaccinations"].mean()
    liste2.append([x,name])
    #print(i,x)

    
liste2.sort(reverse=True)
liste3.append([liste2[0][1],liste2[1][1],liste2[2][1]])
print(liste3)
