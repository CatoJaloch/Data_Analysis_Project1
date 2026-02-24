import pandas as pd
import matplotlib.pyplot as plt

# Load CSVs
Chui_2025 = pd.read_csv("Chui_2025.csv", parse_dates=['reading_date'])
Chui_2026 = pd.read_csv("Chui_2026.csv", parse_dates=['reading_date'])

# Keep relevant columns
cols = ['reading_date', 'temperature_max', 'temperature_min']
Chui_2025 = Chui_2025[cols]
Chui_2026 = Chui_2026[cols]

# Extract day of month (since data is February only)
Chui_2025['day'] = Chui_2025['reading_date'].dt.day
Chui_2026['day'] = Chui_2026['reading_date'].dt.day

# Compute daily average temperature
Chui_2025['temp_avg'] = (Chui_2025['temperature_max'] + Chui_2025['temperature_min']) / 2
Chui_2026['temp_avg'] = (Chui_2026['temperature_max'] + Chui_2026['temperature_min']) / 2

# Plot
plt.figure(figsize=(12,6))

# 2025 (dashed)
plt.plot(Chui_2025['day'], Chui_2025['temperature_max'], '--', label='Max Temp 2025')
plt.plot(Chui_2025['day'], Chui_2025['temperature_min'], '--', label='Min Temp 2025')
plt.plot(Chui_2025['day'], Chui_2025['temp_avg'], '--', label='Avg Temp 2025')

# 2026 (solid)
plt.plot(Chui_2026['day'], Chui_2026['temperature_max'], label='Max Temp 2026')
plt.plot(Chui_2026['day'], Chui_2026['temperature_min'], label='Min Temp 2026')
plt.plot(Chui_2026['day'], Chui_2026['temp_avg'], label='Avg Temp 2026')

plt.title('Daily Temperature Comparison – February (Day-by-Day)')
plt.xlabel('Day of February')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save instead of showing
plt.savefig("chui_feb_daily_temp_comparison.png", dpi=300)
print("Saved: chui_feb_daily_temp_comparison.png")