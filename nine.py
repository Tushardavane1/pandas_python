# import pandas as pd



# df = pd.read_csv("data.csv")

# print(df)

# df2 = (df["A"])
import numpy as np
import seaborn as sns
 
sns.set(style="white")
 
# Generate a random univariate dataset
rs = np.random.RandomState(10)
d = rs.normal(size=100)
 
# Plot a simple histogram and kde
sns.histplot(d, kde=True, color="m")
