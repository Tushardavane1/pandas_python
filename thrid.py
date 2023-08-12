import pandas as pd 
import numpy as np 
dates = pd.date_range("20230720",periods=6)

print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

print(df)

print(df["A"])
print(df.iloc[[1,2,3],[0,2]])

print(df.to_numpy())

print(df.sort_values(by="B"))

print(df.dropna(how="any"))
print(pd.isna(df))
print(df.mean())


