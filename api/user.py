from lib.db import create_user, find_user
from lib.email import send_email
from lib.log import log
from lib.slack import post_slack_msg
from lib.stringutils import get_random_string


def register_user(name: str, passwd: str, email: str):
    # create an entry in the database
    user = create_user(name, email, passwd)

    # post a Slack msg to sales department
    post_slack_msg(
        "sales",
        f"{user.name} has registered with email address {user.email}.",
    )

    # send a welcome email
    send_email(
        user.name,
        user.email,
        "Welcome",
        f"Thanks for registering, {user.name}!\nRegards, TheCompany",
    )

    # write server log
    log(f"User registered with email {user.email}")


def password_forgotten(email: str):
    # retrieve the user
    user = find_user(email)

    # generate a password reset code
    user.reset_code = get_random_string(5)

    # send a password reset email
    send_email(
        user.name,
        user.email,
        "Your password reset",
        f"To reset your password, use this security code: {user.reset_code}.\
            \nRegards, TheCompany",
    )

    # write server log
    log(f"User with email {user.email} requested a password reset.")
