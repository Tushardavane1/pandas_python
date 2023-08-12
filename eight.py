import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
date = pd.date_range("20230728", periods=12)
df = pd.DataFrame(np.random.randn(12,12), index = date,columns=list("ABCDEFGHIJKY"))
# df.plot()
# plt.show()
df2 = df.rename(columns={"A":"a"})
print(df2.head(3))

df3 = pd.plotting.scatter_matrix(df)
print(df3)