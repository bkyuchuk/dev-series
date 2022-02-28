from lib.db import User
from lib.log import log

from api_v2.event import subscribe


def handle_user_registered_event(user: User):
    log(f"User registered with email {user.email}")


def handle_password_forgotten_event(user: User):
    log(f"User with email {user.email} requested a password reset.")


def handle_user_plan_upgrade_event(user: User):
    log(f"User with email {user.email} has upgraded their plan.")


def setup_log_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgotten", handle_password_forgotten_event)
    subscribe("user_plan_upgrade", handle_user_plan_upgrade_event)
