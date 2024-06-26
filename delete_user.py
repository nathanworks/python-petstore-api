import requests
from _config import var

def delete_user(username,boolean):
    url = f"https://petstore.swagger.io/v2/user/{username}"

    headers = {
        "Content-Type" : "application/json"
    }

    response = requests.delete(url,headers=headers)

    if response.status_code == 200:
        if boolean == 0:
            print(f"[PASSED] User {username} has been deleted.")
        else:
            print(f"[FAILED] User {username} has been deleted")
    elif response.status_code == 404:
        if boolean == 0:
            print(f"[FAILED] User {username} not found")
        else:
            print(f"[PASSED] User {username} not found")
    else:
        print(f"[FAILED]Failed to delete user {username}. Status code: {response.status_code}")

