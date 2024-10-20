import plotly.express as px
from random import randint

# Simulate rolling a die 1,000 times
results = [randint(1, 6) for _ in range(1000)]

# Count frequencies of each result
frequencies = [results.count(value) for value in range(1, 7)]

# Create a bar chart
fig = px.bar(x=range(1, 7), y=frequencies, labels={'x': 'Result', 'y': 'Frequency'})
fig.show()