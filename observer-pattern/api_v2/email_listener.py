from lib.db import User
from lib.email import send_email

from .event import subscribe


def handle_user_registered_event(user: User):
    send_email(
        user.name,
        user.email,
        "Welcome",
        f"Thanks for registering, {user.name}!\nRegards, TheCompany",
    )


def handle_password_forgotten_event(user: User):
    send_email(
        user.name,
        user.email,
        "Your password reset",
        f"To reset your password, use this security code: {user.reset_code}.\
            \nRegards, TheCompany",
    )


def handle_user_plan_upgrade_event(user: User):
    send_email(
        user.name,
        user.email,
        "Thank you",
        f"Thanks for upgrading, {user.name}! You're gonna love it.\
            \nRegards, TheCompany",
    )


def setup_email_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgotten", handle_password_forgotten_event)
    subscribe("user_plan_upgrade", handle_user_plan_upgrade_event)
