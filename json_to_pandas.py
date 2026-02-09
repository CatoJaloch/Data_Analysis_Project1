import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
#json loading
with open("project1.json", "r") as f:
    data = json.load(f)
#convert json to dataframe
df = pd.json_normalize(data)
print(df.info())
print(df.head(10))

