import pandas as pd
import numpy as np 
import json
import matplotlib.pyplot as plt
#json loading
with open("project1.json","r") as f:
    data=json.load(f)
#convert json to dataframe
df=pd.json_normalize(data)
#exporting to excel
df.to_excel("project1_data.xlsx", index=False)



