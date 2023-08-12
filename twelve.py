import pandas as pd 
import numpy as np

date = pd.date_range("20230802",periods=12)
df = pd.DataFrame(np.random.randn(12,4), index=date, columns=list("ABCD"))

df2 = df.loc[(df["A"]<0.3)]
print(df2)
