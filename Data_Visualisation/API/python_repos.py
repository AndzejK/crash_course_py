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

print(f"\Selected information about each repository:")
for repo_dict in repo_dicts:
    """
# Examine 1st repository
repo_dict=repo_dicts[0]
    """
    #print("\nSelected info about the 1st repository")
    print(f"\nID: {repo_dict['id']}")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    #print(f"Created: {repo_dict['created_at']}")
    #print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

"""
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
"""
