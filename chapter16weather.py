from pathlib import Path
import matplotlib.pyplot as plt #type: ignore
from datetime import datetime
import csv

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
    high = int(row[4])  # Index 4 corresponds to 'TMAX'
    highs.append(high)

print(highs)

plt.style.use('seaborn')
fig, ax = plt.subplots()

# Step 5: Plot the high temperatures
ax.plot(highs, color='red')

# Step 6: Customize the plot
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

# Step 7: Extract dates and high temperatures
dates, = []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

# Step 8: Plot dates and temperatures
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Step 9: Format the x-axis with dates
fig.autofmt_xdate()

plt.show()