import requests

owner = 'Pedrecho'
repo = 'development_management'
path = '2202'

headers = {
    # 'Authorization': 'token YOUR_ACCESS_TOKEN',
    'Accept': 'application/vnd.github.v3+json',
}

url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'

response = requests.get(url, headers=headers)
data = response.json()

# Print out directory and file names
for item in data:
    print(f'{item["type"]}: {item["name"]}')
