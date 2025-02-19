import requests

username = 'Dp4011'

token = 'token'

# GitHub API URL to list repositories
url = f'https://api.github.com/users/{username}/repos'

# Make a request to the GitHub API
response = requests.get(url, auth=(username, token))

# Check if the request was successful
if response.status_code == 200:
    repos = response.json()
    print("List of repositories:")
    for repo in repos:
        print(repo['name'])
else:
    print(f"Failed to retrieve repositories: {response.status_code}")
