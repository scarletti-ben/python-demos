
# < ========================================================
# < Imports
# < ========================================================

from requests import Response, post, get, put, delete

# < ========================================================
# < Constants
# < ========================================================

BASE_URL: str = "https://jsonblob.com/api/jsonBlob/"

# < ========================================================
# < Functionality
# < ========================================================

def full_url(identifier: int) -> str:
    """Get the full URL for a given identifier"""
    url: str = f"{BASE_URL}{identifier}"
    return url

def create(data: dict) -> int | None:
    """Create a new JSONBlob and return the identifier integer"""
    response: Response = post(BASE_URL, json = data)
    ok_post: bool = response.status_code == 201
    if ok_post:
        identifier: int = response.headers["Location"].split("/")[-1]
        return identifier

def read(identifier: int) -> dict | None:
    """Read a JSONBlob and return as a Python dictionary"""
    url: str = full_url(identifier)
    response: Response = get(url)
    ok_get: bool = response.status_code == 200
    if ok_get:
        return response.json()
    
def update(identifier: int, data: dict) -> bool:
    """Update a JSONBlob and check for status code 200"""
    url: str = full_url(identifier)
    response: Response = put(url, json = data)
    ok_put: bool = response.status_code == 200
    return ok_put

def destroy(identifier: int) -> bool:
    """Destroy a JSONBlob and check for status code 200"""
    url: str = full_url(identifier)
    response: Response = delete(url)
    ok_delete: bool = response.status_code == 200
    return ok_delete

# < ========================================================
# < Execution
# < ========================================================

if __name__ == "__main__":

    from datetime import datetime
    current_date: str = datetime.now().strftime("%Y-%m-%d")
    current_time: str = datetime.now().strftime("%H:%M:%S")
    milliseconds: str = datetime.now().strftime("%f")[:-3]
    current_data: dict = {"date": f"{current_date} {current_time}.{milliseconds}"}

    identifier: int = 1336348896317857792
    print(f"\nIdentifier: {identifier}\nURL: {full_url(identifier)}\n")
    
    original_data: dict = read(identifier)
    print(f"Original Data: {original_data}\n")

    update(identifier, current_data)
    updated_data: dict = read(identifier)
    print(f"Updated Data: {updated_data}\n")

    # identifier: int = create(current_data)
    # print(f"Created ID: {identifier}\n")
    # created_data: dict = read(identifier)
    # print(f"Created Data: {created_data}\n")

    # destroyed: bool = destroy(identifier)
    # print(f"Destroyed Data: {destroyed}\n")