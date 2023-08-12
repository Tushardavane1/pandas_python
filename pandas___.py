import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
date = pd.date_range("20230801" ,periods=6)
df = pd.DataFrame(np.random.randn(6,6), index = date, columns=["A","B","C","E","D","F"])
print(df)
df1 = df.sort_values(by="A")
print(df1)
df1.plot()
plt.show()
