import pandas as pd
import json
import matplotlib.pyplot as plt

# Load JSON
with open("project1.json", "r") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.json_normalize(data)

# Example: simple bar 
plt.bar(df['image_id'], df['field_id'])  

# Add labels and title
plt.xlabel('Farm ID')
plt.ylabel('Field ID')
plt.title('Field ID of Each Farm')

# Show the plot
plt.show()
