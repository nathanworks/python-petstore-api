import requests
from _config import var 

def logout_user():
    url = "https://petstore.swagger.io/v2/user/logout"

    headers = {
        "Content-Type": "application/json"
    }

    requests.get(url, headers=headers)
    print("User has been logged out.")


