from rules import ValidationRules


class ValidationEngine:

    def __init__(self):

        self.rules = ValidationRules()

    def validate_dataframe(self, df):

        issues = []

        for column in df.columns:

            name = column.lower()

            if "email" in name:

                invalid = (~df[column].apply(self.rules.validate_email)).sum()

                issues.append({
                    "column": column,
                    "invalid_email": int(invalid)
                })

            elif "phone" in name:

                invalid = (~df[column].apply(self.rules.validate_phone)).sum()

                issues.append({
                    "column": column,
                    "invalid_phone": int(invalid)
                })

            elif "age" in name:

                invalid = (~df[column].apply(self.rules.validate_age)).sum()

                issues.append({
                    "column": column,
                    "invalid_age": int(invalid)
                })

            elif "amount" in name or "cost" in name:

                invalid = (~df[column].apply(self.rules.validate_positive)).sum()

                issues.append({
                    "column": column,
                    "invalid_values": int(invalid)
                })

        return issues