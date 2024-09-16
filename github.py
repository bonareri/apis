import requests
from decouple import config
# from configs import username, token

def get_github_repos(username, token):
    url = f"https://api.github.com/users/{username}/repos" 
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    } 
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = response.json()
        #print(repos)
        for repo in repos:
            print(f"Repo Name: {repo['name']}")
            print(f"Description: {repo.get('description', 'No Description')}")
            print(f"Repo Language: {repo['language']}")


    else:
        print(f"Failed to retrieve user data. Status code: {response.status_code}")

username = config('USERNAME')
token = config('TOKEN')
get_github_repos(username, token)
