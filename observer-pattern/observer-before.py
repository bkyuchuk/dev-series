from api.plan import upgrade_plan
from api.user import password_forgotten, register_user

# register a new user
register_user("bogdan", "superSafe1234", "bogdan@test.org")

# send a password reset message
password_forgotten("bogdan@test.org")

# upgrade the plan
upgrade_plan("bogdan@test.org")
