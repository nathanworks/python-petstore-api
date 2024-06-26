import requests
from _config import var

def create_user(username, firstName, lastName, email, password, phone, userStatus):
    url = "https://petstore.swagger.io/v2/user"

    payload = { 
        "username": username,
        "firstName": firstName,  
        "lastName": lastName, 
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": userStatus 
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"[PASSED] User {username} created successfully.")
    else:
        print(f"[FAILED ]Failed to create user {username}. Status code: {response.status_code}")


