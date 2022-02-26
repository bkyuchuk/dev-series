from lib.db import find_patient
from lib.log import log
from lib.sms import send_sms
from lib.stringutils import get_random_string


def request_auth_code(email: str) -> None:
    # retrieve the patient
    patient = find_patient(email)

    # generate auth code
    patient.auth_code = get_random_string(5)

    # send SMS with auth code
    send_sms(
        from_="+49 7865 98712",
        to=f"{patient.phone}",
        body=f"Your auth code is: {patient.auth_code}",
    )

    # write server log
    log(f"Patient with email {email} requested an auth code.")
