import requests
from _config import var 

def login_user(username, password):
    url = "https://petstore.swagger.io/v2/user/login"

    payload = {
        "username": username,
        "password": password
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"User {username} logged in successfully.")
    elif response.status_code == 400:
        print(f"Invalid username or password.")
    else:
        print(f"Failed to log in user {username}. Status code: {response.status_code}")

