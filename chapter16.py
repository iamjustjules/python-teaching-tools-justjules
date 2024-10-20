from pathlib import Path
import csv
import matplotlib.pyplot as plt #type: ignore
import numpy as np #type: ignore

# Step 1: Load the CSV file
path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

# Step 2: Create a CSV reader object
reader = csv.reader(lines)

# Step 3: Get the header row (first line of the CSV file)
header_row = next(reader)
print(header_row)  # Output: ['STATION', 'NAME', 'DATE', 'TAVG', 'TMAX', 'TMIN']

# Step 4: Extract high temperatures
highs = []
for row in reader:
    try: 
        high = int(row[4])  # Index 4 corresponds to 'TMAX'
        highs.append(high)
    except ValueError:
        print(f"This is missing information for the date: {row[2]}") # this will print the date of the missing information


print(highs)

# Step 5: Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, color='red')

# Step 6: Customize the plot
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

print(plt.style.available) # this will show the available styles for the plot