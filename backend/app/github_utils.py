import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_pr_diff(owner: str, repo: str, pr_number: int):
    """
    Fetch raw PR diff from GitHub API
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3.diff"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print("❌ Failed to fetch PR diff:", response.status_code)
        print(response.text)
        return None