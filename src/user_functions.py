# The simplest function to get the user email (copy to src/user_functions.py)
from string import printable
import re


def get_email_from_input():
    """ Contains '@' and '.' """
    return input("Write down your email: ")


# More elaborated version (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Write down your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email


def get_user_name_from_input():
    """ Not empty string. No spaces. """
    username = input("Write down your username: ")
    if bool(re.search(r"\s", username)):
        print("Invalid username")
    else:
        return username


def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one
    letter."""
    password = input("Write down your password: ")
    if len(password) >= 8 and re.search('[a-zA-Z]', password) and re.findall('[^A-Za-z0-9]', password)and any(str.isdigit(c) for c in password):
        return password
    else:
        print("Invalid password")
