import requests
from _config import var

def get_user(username,boolean):
    url = f"https://petstore.swagger.io/v2/user/{username}"

    headers = {
        "Content-Type" : "application/json"
    }

    response = requests.get(url,headers=headers)

    if response.status_code == 200 and boolean == 0 :
        print(f"[PASSED] User {username} is exist.")
    elif response.status_code == 404:
        if boolean == 0:
            print(f"[FAILED] User {username} not found")
        else:
            print(f"[PASSED] User {username} not found")
    else:
        print(f"[FAILED] Failed to get user {username}. Status code: {response.status_code}")
