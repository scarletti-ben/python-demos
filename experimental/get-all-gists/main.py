
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

# def get_all_gist_metadata(username: str) -> list[dict] | None:
#     """Get all public gists from GitHub for a given user"""
#     url: str = f"https://api.github.com/users/{username}/gists"
#     response: Response = requests.get(url)
#     if response.status_code == 200:
#         all_metadata: list[dict] = response.json()
#         return all_metadata
    
# def get_gist_urls(metadata_list: list[dict]) -> list[dict] | None:
#     """Get all gist URLs from the main metadata list"""
#     gist_urls: list[str] = [metadata["html_url"] for metadata in metadata_list]
#     return gist_urls

# def get_files_in_gist(url: str) -> dict[str, str] | None:
#     """Get a dictionary for all files in a given gist"""
#     response: Response = requests.get(url)
#     if response.status_code == 200:
#         metadata: dict = response.json()
#         output: dict = {}
#         for file_name, file_info in metadata["files"].items():
#             raw_url: str = file_info["raw_url"]
#             output[file_name] = raw_url
#         return output
    
# def get_text_from_raw_url(raw_url: str) -> str | None:
#     """Get the raw text string from a raw file URL"""
#     response: dict = requests.get(raw_url)
#     if response.status_code == 200:
#         return response.text

def get_clean_dictionary(username: str) -> dict | None:
    """Get all public gists from GitHub for a given user"""
    url: str = f"https://api.github.com/users/{username}/gists"
    response: Response = requests.get(url)
    if response.status_code == 200:
        all_metadata: list[dict] = response.json()
        clean_gist_dictionary: dict = {}
        for gist_metadata in all_metadata:
            gist_id: int = gist_metadata["id"]
            gist_description: str = gist_metadata["description"]
            gist_files_dictionary: dict = gist_metadata["files"]
            clean_files_dictionary: dict = {}
            for file_name, file_dictionary in gist_files_dictionary.items():
                file_url: str = file_dictionary["raw_url"]
                clean_files_dictionary[file_name] = file_url
            clean_gist_dictionary[gist_id] = {
                "description": gist_description,
                "files": clean_files_dictionary
            }
        return clean_gist_dictionary

def pretty_print(item, indent = 0):
    """Recursively pretty-print dictionaries and iterables"""

    separator = '\n' + '-' * 79 + '\n'
    tab = '    '

    if indent == 0:
        print(separator)

    item = getattr(item, '__dict__', item)

    if isinstance(item, dict):
        for key, value in item.items():
            print(f"{tab * indent}{key}: ", end = "")
            if isinstance(value, (dict, list, tuple, set)):
                print()
                pretty_print(value, indent + 1)
                if indent == 0:
                    print()
            else:
                print(value)
    elif isinstance(item, (list, tuple, set)):
        print(f"{tab * indent}" + ", ".join(map(str, item)))
    else:
        print(f"{tab * indent}{item}")

    if indent == 0:
        print(separator)

if __name__ == "__main__":

    core_dictionary: dict = get_clean_dictionary(username)
    pretty_print(core_dictionary)

    for gist_identifier, gist_dictionary in core_dictionary.items():
        print(f"ID: {gist_identifier} -> Description: {gist_dictionary["description"]} ->")
        for file_name, file_url in gist_dictionary["files"].items():
            print(f"    File: {file_name} -> URL: {file_url}")
    
    print("\n\n")