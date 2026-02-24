import pandas as pd

# Load the CSVs
Chui_2025 = pd.read_csv("Chui_2025.csv", parse_dates=['reading_date'])
Chui_2026 = pd.read_csv("Chui_2026.csv", parse_dates=['reading_date'])

# Focus on relevant columns
cols = ['reading_date', 'temperature_max', 'temperature_min']
Chui_2025 = Chui_2025[cols]
Chui_2026 = Chui_2026[cols]

# Calculate daily average temperature
Chui_2025['temp_avg'] = (Chui_2025['temperature_max'] + Chui_2025['temperature_min']) / 2
Chui_2026['temp_avg'] = (Chui_2026['temperature_max'] + Chui_2026['temperature_min']) / 2

# Calculate overall average temperature for February
avg_temp_2025 = Chui_2025['temp_avg'].mean()
avg_temp_2026 = Chui_2026['temp_avg'].mean()

print(f"February Average Temperature (°C) - 2025: {avg_temp_2025:.2f}, 2026: {avg_temp_2026:.2f}")

# Calculate daily temperature range
Chui_2025['temp_range'] = Chui_2025['temperature_max'] - Chui_2025['temperature_min']
Chui_2026['temp_range'] = Chui_2026['temperature_max'] - Chui_2026['temperature_min']

# Calculate overall average range for February
avg_range_2025 = Chui_2025['temp_range'].mean()
avg_range_2026 = Chui_2026['temp_range'].mean()

print(f"February Average Temperature Range (°C) - 2025: {avg_range_2025:.2f}, 2026: {avg_range_2026:.2f}")