import pandas as pd 
import numpy as np

df = pd.DataFrame({
    "Name":["Tushar","Abhi","Sachin","Amol"],
    "Age":[21,8,40,12],
    "Lang":["python","java","js","go"],
    "rank":[1,2,3,4]
})
print(df)

table = pd.pivot_table(df, values='Name', index=['rank', 'Age'],
                       columns=['Lang'], aggfunc=np.sum)
print(table)

#value function in the pandas
print(df["Age"].value_counts())
#group function the pandas 
print(df.groupby("Age").sum().plot(kind="bar"))

#loc and iloc function in the pandas 
print(df.loc[df.Age>=20])

#fitering the multiple columns in pandas using the loc function

df2 = df.loc[:,"Age"]
print(df2)
#unquie and nuquie in python pandas 
df3 = df["Age"].unique()
print(df3)

df4 = df["Age"].nunique()
print(df4)

# iterate through each row and select
# 'Name' and 'Stream' column respectively using the for loop in pandas python 
for ind in df.index:
    print(df['Name'][ind], df['rank'][ind])