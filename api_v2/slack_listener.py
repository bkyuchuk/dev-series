from lib.db import User
from lib.slack import post_slack_msg

from .event import subscribe


def handle_user_registered_event(user: User):
    post_slack_msg(
        "sales",
        f"{user.name} has registered with email address {user.email}.",
    )


def setup_slack_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
