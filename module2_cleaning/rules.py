import re
import pandas as pd


class ValidationRules:

    EMAIL_PATTERN = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    def validate_email(self, email):

        if pd.isna(email):
            return False

        return bool(re.match(self.EMAIL_PATTERN, str(email)))

    def validate_phone(self, phone):

        if pd.isna(phone):
            return False

        phone = str(phone)

        return phone.isdigit() and len(phone) == 10

    def validate_positive(self, value):

        if pd.isna(value):
            return False

        return value > 0

    def validate_age(self, age):

        if pd.isna(age):
            return False

        return 0 <= age <= 120