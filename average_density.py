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
df_exploded= df.explode('growth_stages')
df_stages =pd.json_normalize(df_exploded['growth_stages'])
avg_density = (
    df_stages
    .groupby('name')['density']
    .mean()
)
print(avg_density)
avg_density_df = avg_density.to_frame().T


field_id = df['field_id'].iloc[0]
variety_id = df['image.farm_id'].iloc[0]
created_at = df['created_at'].iloc[0]


avg_density_df.insert(0, 'created_at', created_at)
avg_density_df.insert(0, 'variety_id', variety_id)
avg_density_df.insert(0, 'field_id', field_id)

avg_density_df.to_excel("average_densities.xlsx", index=False)