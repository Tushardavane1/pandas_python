import pandas as pd

df = {
    "Name" : ["Tushar","Tushar","Tushar"],
    "Age": [12,34,56]
}

df1 = pd.DataFrame(df)
print(df1)


df2 = df1.loc[:, ["Name", "Age"]]

print(df1.iloc[1, 1])

print(type(df1))

print(df1.describe())

print(df2)