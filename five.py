import pandas as pd 
dates = pd.date_range("20230721",periods=4)
df = pd.DataFrame({

     "A":["Tushar","Abhi","Amol","Sachin"],
     "B":[87,89,88,78],
     "C":[1,2,3,4]
},index=dates)
print(df)