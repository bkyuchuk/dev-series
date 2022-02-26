from lib.db import create_patient, find_patient
from lib.email import send_email
from lib.log import log


def register_patient(name: str, phone: str, email: str) -> None:
    # create an entry in the database
    patient = create_patient(name, phone, email)

    # send a confirmation email
    send_email(
        patient.name,
        patient.email,
        "Welcome",
        f"You have successfully registered, {patient.name}.\n"
        "Best regards, Charlot Hospital",
    )

    # write server log
    log(f"Patient registered with email {patient.email}")


def make_appointment(email: str, date: str) -> None:
    # retrieve the patient
    patient = find_patient(email)

    # set the patient's appointment
    patient.appointment = date

    # send confirmation email
    send_email(
        patient.name,
        patient.email,
        "Appointment Confirmation",
        f"Your appointment for {date} has been registered.\n"
        "Best regards, Charlot Hospital",
    )

    # write server log
    log(f"Patient with email {email} created an appointment for {date}.")
