
# < ========================================================
# < Imports
# < ========================================================

import requests
from requests import Response

# < ========================================================
# < Constants and Variables
# < ========================================================

username: str = "scarletti-ben"

# < ========================================================
# < Functionality
# < ========================================================

def get_all_gists(username: str) -> list[dict] | None:
    """Get all public gists from GitHub for a given user"""
    url: str = f"https://api.github.com/users/{username}/gists"
    response: Response = requests.get(url)
    if response.status_code == 200:
        gists: list[dict] = response.json()
        return gists
    
# < ========================================================
# < Execution
# < ========================================================

if __name__ == "__main__":
    gists: list[dict] = get_all_gists(username)
    print(gists)