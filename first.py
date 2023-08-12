import pandas as pd 
import numpy as np

dict ={
    "Students":["Tushar","Rohan","Abhi","Amol"],
    "Marks":[12,34,56,67]
}
df = pd.DataFrame(dict)
print(df)

df.index =  ["first","second","thirth","fourth"]
print(df)

df1 = df.to_excel("first1.xlsx",index=False)
#df2 = df.describe()
#print(df2)
