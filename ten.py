import pandas as pd 
import numpy as np

df = pd.DataFrame(np.random.randn(12,4), columns = list("ABCD") )  
print(df)