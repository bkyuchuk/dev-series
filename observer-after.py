from api_v2.email_listener import setup_email_event_handlers
from api_v2.log_listener import setup_log_event_handlers
from api_v2.plan import upgrade_plan
from api_v2.slack_listener import setup_slack_event_handlers
from api_v2.user import password_forgotten, register_user

setup_log_event_handlers()
setup_email_event_handlers()
setup_slack_event_handlers()

# register a new user
register_user("bogdan", "superSafe1234", "bogdan@test.org")

# send a password reset message
password_forgotten("bogdan@test.org")

# upgrade the plan
upgrade_plan("bogdan@test.org")
