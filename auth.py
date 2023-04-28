import requests
import json


def Login(auth, email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user
    except requests.exceptions.HTTPError as err:
        errorMessage = json.loads(err.args[1])["error"]["message"]
        print(errorMessage)
        if errorMessage == "INVALID_EMAIL":
            print("Invalid email!")
        elif errorMessage == "EMAIL_NOT_FOUND":
            print("Email not found!")
        elif errorMessage == "INVALID_PASSWORD":
            print("Incorrect password!")
        elif errorMessage == "USER_DISABLED":
            print("User disabled!")
        elif errorMessage == "TOO_MANY_ATTEMPTS_TRY_LATER":
            print("Too many attempts! Try again later!")
        return None


def Register(auth, email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return user
    except requests.exceptions.HTTPError as err:
        errorMessage = json.loads(err.args[1])["error"]["message"]
        if errorMessage == "INVALID_EMAIL":
            print("Invalid email!")
        elif errorMessage == "WEAK_PASSWORD":
            print("Weak password!")
        elif errorMessage == "EMAIL_EXISTS":
            print("Email already exists!")
        return None

