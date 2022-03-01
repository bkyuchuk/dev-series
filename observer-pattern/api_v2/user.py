from lib.db import create_user, find_user
from lib.stringutils import get_random_string

from .event import post_event


def register_user(name: str, passwd: str, email: str):
    # create an entry in the database
    user = create_user(name, email, passwd)

    # fire a user registered event
    post_event("user_registered", user)


def password_forgotten(email: str):
    # retrieve the user
    user = find_user(email)

    # generate a password reset code
    user.reset_code = get_random_string(5)

    # fire a password forgotten event
    post_event("user_password_forgotten", user)


def reset_password(code: str, email: str, password: str):
    # retrieve the user
    user = find_user(email)

    # reset the password
    user.reset_password(code, password)
