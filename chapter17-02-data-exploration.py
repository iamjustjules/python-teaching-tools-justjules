import requests
import plotly.express as px

# API call to GitHub for popular Python projects
url = "https://api.github.com/search/repositories?q=language:python+sort:stars"
response = requests.get(url)
response_data = response.json()

# Create lists for repository names and star counts
repositories = response_data['items']
repo_names = []
stars = []

for repo in repositories:
    repo_names.append(repo['name'])
    stars.append(repo['stargazers_count'])

# Create a bar chart
fig = px.bar(x=repo_names, y=stars, title="Most-Starred Python Projects on GitHub", labels={'x':'Repository', 'y':'Stars'})
fig.show()
