from _config import var
from create_user import create_user
from login import login_user
from logout import logout_user
from delete_user import delete_user

username = var["username"]
password = var["password"]
firstName = var["firstName"]
lastName = var["lastName"]
email = var["email"]
phone = var["phone"]
status = var["userStatus"]

updateUsername = var["updateUsername"]
updateEmail = var["updateEmail"]

boolean = 0

create_user(
    username,
    firstName,
    lastName,
    email,
    password,
    phone,
    status
)
login_user(
    username,
    password
)

logout_user()

delete_user(
    username,
    boolean
)