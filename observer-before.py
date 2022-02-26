from api.auth import request_auth_code
from api.patient import make_appointment, register_patient

# register a new patient
register_patient("Bogdan Kyuchukov", "+49 1876 66451", "bogdan@test.org")

# request auth code
request_auth_code("bogdan@test.org")

# make an appointment
make_appointment("bogdan@test.org", "03/19/2022 18:00")
