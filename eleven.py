import pandas as pd 
df = pd.read_csv("jswsteel.csv", usecols=["HIGH"])
print(df)