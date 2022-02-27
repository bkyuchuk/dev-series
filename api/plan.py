from lib.db import find_user
from lib.email import send_email
from lib.log import log
from lib.slack import post_slack_msg


def upgrade_plan(email: str):
    # find the user
    user = find_user(email)

    # upgrade the plan
    user.plan = "paid"

    # post a Slack msg to sales department
    post_slack_msg("sales", f"{user.name} has upgraded their plan.")

    # send a thank you email
    send_email(
        user.name,
        user.email,
        "Thank you",
        f"Thanks for upgrading, {user.name}! You're gonna love it.\
            \nRegards, TheCompany",
    )

    # write a server log
    log(f"User with email {user.email} has upgraded their plan.")
