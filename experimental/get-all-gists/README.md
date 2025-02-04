# Get All Gists
## Overview
You can use the `GitHub` `API` to access all public `gists` for a given user

This is easily achieved in `Python` via `requests.get(https://api.github.com/users/{username}/gists)`, which will return a list of dictionaries of all the `gists` for that username