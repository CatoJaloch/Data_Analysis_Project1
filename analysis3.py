import pandas as pd
import matplotlib.pyplot as plt

# Farm file info: key = farm name, value = list of CSVs for 2025 and 2026
farms = {
    "Chui": ["Chui_2025.csv", "Chui_2026.csv"],
    "Elgon": ["Elgon_2025.csv", "Elgon_2026.csv"],
    "Maasai": ["Maasai_2025.csv", "Maasai_2026.csv"]
}

# Process each farm
for farm, files in farms.items():
    # Load CSVs
    df_2025 = pd.read_csv(files[0], parse_dates=['reading_date'])
    df_2026 = pd.read_csv(files[1], parse_dates=['reading_date'])
    
    # Keep relevant columns
    cols = ['reading_date', 'temperature_max', 'temperature_min']
    df_2025 = df_2025[cols]
    df_2026 = df_2026[cols]
    
    # Extract day of month (February only)
    df_2025['day'] = df_2025['reading_date'].dt.day
    df_2026['day'] = df_2026['reading_date'].dt.day
    
    # Compute daily average temperature
    df_2025['temp_avg'] = (df_2025['temperature_max'] + df_2025['temperature_min']) / 2
    df_2026['temp_avg'] = (df_2026['temperature_max'] + df_2026['temperature_min']) / 2
    
    # Compute daily temperature range
    df_2025['temp_range'] = df_2025['temperature_max'] - df_2025['temperature_min']
    df_2026['temp_range'] = df_2026['temperature_max'] - df_2026['temperature_min']
    
    # Compute overall averages for February
    avg_temp_2025 = df_2025['temp_avg'].mean()
    avg_temp_2026 = df_2026['temp_avg'].mean()
    avg_range_2025 = df_2025['temp_range'].mean()
    avg_range_2026 = df_2026['temp_range'].mean()
    
    # Print summary
    print(f"\n=== {farm} – February Temperature Summary ===")
    print(f"Average Temp (°C) – 2025: {avg_temp_2025:.2f}, 2026: {avg_temp_2026:.2f}")
    print(f"Average Temp Range (°C) – 2025: {avg_range_2025:.2f}, 2026: {avg_range_2026:.2f}")
    
    # Plot daily comparison
    plt.figure(figsize=(12,6))
    
    # 2025 (dashed)
    plt.plot(df_2025['day'], df_2025['temperature_max'], '--', label='Max Temp 2025')
    plt.plot(df_2025['day'], df_2025['temperature_min'], '--', label='Min Temp 2025')
    plt.plot(df_2025['day'], df_2025['temp_avg'], '--', label='Avg Temp 2025')
    
    # 2026 (solid)
    plt.plot(df_2026['day'], df_2026['temperature_max'], label='Max Temp 2026')
    plt.plot(df_2026['day'], df_2026['temperature_min'], label='Min Temp 2026')
    plt.plot(df_2026['day'], df_2026['temp_avg'], label='Avg Temp 2026')
    
    plt.title(f'Daily Temperature Comparison – {farm} – February')
    plt.xlabel('Day of February')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # Save figure
    filename = f"{farm.lower()}_feb_daily_temp_comparison.png"
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"Saved plot: {filename}")