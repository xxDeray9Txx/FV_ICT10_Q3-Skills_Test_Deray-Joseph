from pyscript import document, display
import re

def create_account(e):
    # Get inputs from fields
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    result = document.getElementById("result")

    # Validate username (minimum 7 characters)
    if len(username) >= 7:
        username_msg = "Username accepted."
    else:
        username_msg = "Username must be at least 7 characters long."

    # Validate password (minimum 10 characters, at least 1 letter and 1 number)
    has_letter = re.search(r"[A-Za-z]", password) is not None
    has_digit = re.search(r"\d", password) is not None

    if len(password) >= 10 and has_letter and has_digit:
        password_msg = "Password accepted."
    else:
        password_msg = "Password must be at least 10 characters long and include at least 1 letter and 1 number."

    # Show combined result
    result.innerText = f"{username_msg}\n{password_msg}"