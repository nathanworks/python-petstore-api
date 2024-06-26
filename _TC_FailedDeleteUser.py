from _config import var
from create_user import create_user
from login import login_user
from logout import logout_user
from delete_user import delete_user
from get_user import get_user

username = var["username"]
password = var["password"]
firstName = var["firstName"]
lastName = var["lastName"]
email = var["email"]
phone = var["phone"]
status = var["userStatus"]

updateUsername = var["updateUsername"]
updateEmail = var["updateEmail"]

boolean = 1

delete_user(
    username,
    boolean
)
