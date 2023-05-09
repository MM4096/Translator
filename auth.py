import requests
import json
from enum import Enum


class ReturnEnum(Enum):
    SUCCESS = "SUCCESS"
    INVALID_EMAIL = "INVALID_EMAIL"
    INVALID_PASSWORD = "INVALID_PASSWORD"
    EMAIL_NOT_FOUND = "EMAIL_NOT_FOUND"
    USER_DISABLED = "USER_DISABLED"
    TOO_MANY_ATTEMPTS_TRY_LATER = "TOO_MANY_ATTEMPTS_TRY_LATER"
    WEAK_PASSWORD = "WEAK_PASSWORD"
    EMAIL_EXISTS = "EMAIL_EXISTS"


def Login(auth, email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user, ReturnEnum.SUCCESS
    except requests.exceptions.HTTPError as err:
        errorMessage = json.loads(err.args[1])["error"]["message"]
        if errorMessage == "INVALID_EMAIL":
            return None, ReturnEnum.INVALID_EMAIL
        elif errorMessage == "EMAIL_NOT_FOUND":
            return None, ReturnEnum.EMAIL_NOT_FOUND
        elif errorMessage == "INVALID_PASSWORD":
            return None, ReturnEnum.INVALID_PASSWORD
        elif errorMessage == "USER_DISABLED":
            return None, ReturnEnum.USER_DISABLED
        elif errorMessage == "TOO_MANY_ATTEMPTS_TRY_LATER":
            return None, ReturnEnum.TOO_MANY_ATTEMPTS_TRY_LATER
        return None


def Register(auth, email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        auth.send_email_verification(user['idToken'])
        return user, ReturnEnum.SUCCESS
    except requests.exceptions.HTTPError as err:
        errorMessage = json.loads(err.args[1])["error"]["message"]
        if errorMessage == "INVALID_EMAIL":
            return None, ReturnEnum.INVALID_EMAIL
        elif errorMessage == "WEAK_PASSWORD":
            return None, ReturnEnum.WEAK_PASSWORD
        elif errorMessage == "EMAIL_EXISTS":
            return None, ReturnEnum.EMAIL_EXISTS
        return None


def ForgotPassword(auth, email):
    try:
        auth.send_password_reset_email(email)
        return ReturnEnum.SUCCESS
    except requests.exceptions.HTTPError as err:
        errorMessage = json.loads(err.args[1])["error"]["message"]
        if errorMessage == "EMAIL_NOT_FOUND":
            return ReturnEnum.EMAIL_NOT_FOUND
        return None
