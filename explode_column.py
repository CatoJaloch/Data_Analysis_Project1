import pandas as pd
import numpy as np 
import json
import matplotlib.pyplot as plt

#json loading
with open("project1.json","r") as f:
    data=json.load(f)

#convert json to dataframe
df=pd.json_normalize(data)

#open the columns within a column
df_exploded= df.explode('growth_stages')
df_stages =pd.json_normalize(df_exploded['growth_stages'])

# display the exploded columns with names
for col in df_stages.columns:
    print(col)
print(df_stages.head())    

# creation oif excel sheet with exploded columns
df_stages.to_excel("growth_stages.xlsx", index=False)
