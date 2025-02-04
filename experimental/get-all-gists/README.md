# Get All Gists
## Overview
You can use the `GitHub` `API` to access all public `gists` for a given user

This is easily achieved in `Python` via `requests.get(https://api.github.com/users/{username}/gists)`, which will return a list of dictionaries of all the `gists` for that username

An example, abridged, log output for a user with only one `gist`
```powershell
[{'url': 'https://api.github.com/gists/{id}', 'forks_url': 'https://api.github.com/gists/{id}/forks', 'commits_url': 'https://api.github.com/gists/{id}/commits', 'id': '{id}', 'node_id': 'G_kwDOCMAZpxoAIGZjNDRlY2NjNxI1YTIzYjllYjNhYmYwOGM4YzBiZWQx', 'git_pull_url': 'https://gist.github.com/{id}.git', 'git_push_url': 'https://gist.github.com/{id}.git', 'html_url': 'https://gist.github.com/username/{id}', 'files': {'test.py': {'filename': 'test.py', 'type': 'application/x-python', 'language': 'Python', 'raw_url': 'https://gist.githubusercontent.com/username/{id}/raw/48137ab03450d53x4301xe3fc35853fd1e0fcd2f/test.py', 'size': 116}}, 'public': True, 'created_at': '2025-02-04T17:46:20Z', 'updated_at': '2025-02-04T17:46:21Z', 'description': 'test gist', 'comments': 0, 'user': None, 'comments_enabled': True, 'comments_url': 'https://api.github.com/gists/{id}/comments', 'owner': {'login': 'username', 'id': 146817206, 'node_id': 'U_kgDcXMAZpg', 'avatar_url': 'https://avatars.githubusercontent.com/u/146217206?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/username', 'html_url': 'https://github.com/username', 'followers_url': 'https://api.github.com/users/username/followers', 'following_url': 'https://api.github.com/users/username/following{/other_user}', 'gists_url': 'https://api.github.com/users/username/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/username/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/username/subscriptions', 'organizations_url': 'https://api.github.com/users/username/orgs', 'repos_url': 'https://api.github.com/users/username/repos', 'events_url': 'https://api.github.com/users/username/events{/privacy}', 'received_events_url': 'https://api.github.com/users/username/received_events', 'type': 'User', 'user_view_type': 'public', 'site_admin': False}, 'truncated': False}]
```

Cleaned up output with new method
```powershell

-------------------------------------------------------------------------------

fc44eccc725a23b9eb3abf08c8c0bed1: 
    description: test gist
    files: 
        test.py: https://gist.githubusercontent.com/scarletti-ben/fc44eccc725a23b9eb3abf08c8c0bed1/raw/48137ab03450d53f4301ce3fc35853fd1e0fcd2f/test.py


-------------------------------------------------------------------------------

ID: fc44eccc725a23b9eb3abf08c8c0bed1 -> Description: test gist ->
    File: test.py -> URL: https://gist.githubusercontent.com/scarletti-ben/fc44eccc725a23b9eb3abf08c8c0bed1/raw/48137ab03450d53f4301ce3fc35853fd1e0fcd2f/test.py

```