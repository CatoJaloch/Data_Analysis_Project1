import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("farm_field_variety_summary.csv")

# Count the number of fields in each size category
size_counts = df['field_size_category'].value_counts()

# Optional: ensure all categories are included, even if count = 0
categories = ["small", "medium", "large", "Uncategorised"]
size_counts = size_counts.reindex(categories, fill_value=0) 

# Plot pie chart
plt.figure(figsize=(7, 7)) 
plt.pie(
    size_counts,
    labels=size_counts.index, 
    autopct="%5.1f%%",  
    startangle=90, 
    colors=["green", "blue","red", "yellow"]  
)
plt.title("Distribution of Field Sizes")
plt.savefig("field_size_distribution.png")
print("Pie chart saved: field_size_distribution.png")

# Count occurrences of each variety
variety_counts = df['variety_name'].value_counts()

# Plot horizontal bar chart
plt.figure(figsize=(10, 8))
variety_counts.plot(kind='barh', color='skyblue')
plt.xlabel("Number of Fields")
plt.ylabel("Variety Name")
plt.title("Distribution of Field Varieties")
plt.gca().invert_yaxis()  # largest on top
plt.tight_layout()
plt.savefig("variety_distribution.png")