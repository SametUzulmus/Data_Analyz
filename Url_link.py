data={
    "Device_Type":("AX0145","TRU151","ZOD231","YRT326","LWR245"),
    "Stats_Access_Link":("<url>https://xcd32112.smart_meter.com</url>",
                         "<url>http://tXh67.dia_meter.com</url>",
                         "<url>http://yT5495.smart_meter.com</url>",
                         "<url>https://ret323_TRu.crown.com</url>",
                         "<url>http://luwr3243.celcius.com</url>")
}

# xcd32112.smart_meter.com

df=pd.DataFrame(data,index=[i for i in range(1,6)])

df["Stats_Access_Link"]=df["Stats_Access_Link"].str.replace("<url>https://","")
df["Stats_Access_Link"]=df["Stats_Access_Link"].str.replace("<url>http://","")
df["Stats_Access_Link"]=df["Stats_Access_Link"].str.replace("</url>","")

liste=[]
liste2=[]

for i in df["Stats_Access_Link"]:
    liste.append(i)

for i in df["Device_Type"]:
    liste2.append(i)

data2=dict(zip(liste2,liste))
print(data2["AX0145"]) # Output = xcd32112.smart_meter.com
