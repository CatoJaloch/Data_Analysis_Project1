import pandas as pd 
import json
import numpy as np
import matplotlib.pyplot as plt #for plotting

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

avg_density_df = avg_density.to_frame().T


field_id = df['field_id'].iloc[0] #since all rows have same field_id, take the first one just
variety_id = df_stages['variety_id'].iloc[0]
capture_date = df['image.capture_date'].iloc[0]
farm_id =df['image.farm_id'].iloc[0]

avg_density_df.insert(0, 'farm_id', farm_id)
avg_density_df.insert(0, 'field_id', field_id)
avg_density_df.insert(0, 'variety_id', variety_id)
avg_density_df.insert(0, 'capture_date', capture_date)

minidataset_df = pd.read_csv("minidataset.csv")
print(minidataset_df.head())

avg_density_df = avg_density_df.merge(minidataset_df[["id","variety_name","area_msqr","type"]],
    left_on="field_id",
    right_on="id",
    how="left"
)
# avg_density_df = avg_density_df.drop(columns=["variety_id_y","farm_id_y"])
# avg_density_df = avg_density_df.rename(columns={"variety_id_x": "variety_id", "farm_id_x": "farm_id"})
avg_density_df = avg_density_df.drop(columns=["id"])    




avg_density_df.to_excel("average_densities.xlsx", index=False)
