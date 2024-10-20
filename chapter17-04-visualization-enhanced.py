import requests
import plotly.express as px

# API call to GitHub for popular Python projects
url = "https://api.github.com/search/repositories?q=language:python+sort:stars"
response = requests.get(url)
response_data = response.json()

# Create lists for repository names, star counts, and hover text
repositories = response_data['items']
repo_names = []
stars = []
hover_text = []

for repo in repositories:
    repo_names.append(repo['name'])
    stars.append(repo['stargazers_count'])
    # Properly format the hover text on a single line
    hover_text.append(f"{repo['owner']['login']} - {repo['description']}")

# Create a bar chart with hover text
fig = px.bar(x=repo_names, y=stars, title="Most-Starred Python Projects on GitHub", labels={'x':'Repository', 'y':'Stars'})
fig.update_traces(hovertext=hover_text)

# Add custom title and axis labels
fig.update_layout(title="Most-Starred Python Projects", xaxis_title="Repository", yaxis_title="Stars")
fig.show()
