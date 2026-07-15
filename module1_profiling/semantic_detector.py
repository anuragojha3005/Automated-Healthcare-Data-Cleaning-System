class SemanticDetector:

    def detect(self, column_name):

        column = column_name.lower()

        rules = {

            "patient_id": "Patient Identifier",
            "doctor_id": "Doctor Identifier",
            "appointment_id": "Appointment Identifier",
            "treatment_id": "Treatment Identifier",
            "bill_id": "Billing Identifier",

            "first_name": "Person Name",
            "last_name": "Person Name",

            "email": "Email Address",

            "contact_number": "Phone Number",
            "phone_number": "Phone Number",

            "address": "Address",

            "date_of_birth": "Birth Date",
            "registration_date": "Registration Date",
            "appointment_date": "Appointment Date",
            "treatment_date": "Treatment Date",
            "bill_date": "Billing Date",

            "cost": "Treatment Cost",
            "amount": "Billing Amount",

            "insurance_provider": "Insurance Provider",
            "insurance_number": "Insurance Number"

        }

        return rules.get(column, "Unknown")


def detect_pii(column_name):

    column = column_name.lower()

    pii_keywords = [

        "name",
        "email",
        "phone",
        "contact",
        "address",
        "insurance"

    ]

    for keyword in pii_keywords:

        if keyword in column:
            return True

    return False        