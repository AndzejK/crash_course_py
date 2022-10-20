from email import header
import requests

# Make an API call and store the response
url="https://api.github.com/search/repositories?q=language:python&sort=stars"
headers={"Accept":"application/vnd.github.v3+json"}
r=requests.get(url,headers=headers)
print(f"status cose: {r.status_code}")

# Store API response in variable - APIs are here now
response_dict=r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories
repo_dicts=response_dict['items']
print(f"Repositories returned {len(repo_dicts)}")

# Examine 1st repository
repo_dict=repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
