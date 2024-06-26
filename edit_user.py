import requests
from _config import var

def edit_user(username, updateUsername, firstName, lastName, updateEmail, password, phone, userStatus):
    url = f"https://petstore.swagger.io/v2/user/{username}"

    payload = { 
        "username": updateUsername,
        "firstName": firstName,  
        "lastName": lastName, 
        "email": updateEmail,
        "password": password,
        "phone": phone,
        "userStatus": userStatus 
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.put(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"User {username} has been successfully updated.")
    elif response.status_code == 404:
        print(f"User {username} not found")
    else:
        print(f"Failed to update user {username}. Status code: {response.status_code}")

edit_user(var["username"],var['updateUsername'],var["firstName"],var["lastName"],var["updateEmail"],var["password"],var["phone"],var["userStatus"])
