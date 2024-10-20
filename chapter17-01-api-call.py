import requests

# API call to GitHub for popular Python projects
url = "https://api.github.com/search/repositories?q=language:python+sort:stars"
response = requests.get(url)

# Check if the API call was successful (status code 200 means success)
if respons.status_ceode == 200:
    print(f"Status code: {response.status_code} - API call successful!")
else:
    print(f"Status code: {response.status_code} - API call failed!")

# Convert the response to a Python dictionary (using JSON format)
response_data = response.json()

# Explore the keys of the response
print(response_data.keys())
