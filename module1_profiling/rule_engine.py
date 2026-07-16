import re


class RuleEngine:

    def analyze(self, df):

        report = {}

        warnings = []

        pii_columns = []

        suspicious_columns = []

        # Suspicious Column Names
        suspicious_keywords = [
            "password",
            "secret",
            "token",
            "otp",
            "pin"
        ]

        # PII Keywords
        pii_keywords = [
            "name",
            "email",
            "phone",
            "contact",
            "address",
            "insurance"
        ]

        for column in df.columns:

            lower = column.lower()

            # Suspicious columns
            for key in suspicious_keywords:

                if key in lower:
                    suspicious_columns.append(column)

            # PII columns
            for key in pii_keywords:

                if key in lower:
                    pii_columns.append(column)

        report["pii_columns"] = list(set(pii_columns))

        report["suspicious_columns"] = list(set(suspicious_columns))

        # Duplicate rows

        duplicates = int(df.duplicated().sum())

        report["duplicate_rows"] = duplicates

        if duplicates > 0:

            warnings.append(
                f"{duplicates} duplicate rows found"
            )

        report["warnings"] = warnings

        # -----------------------------
        # Data Quality Score
        # -----------------------------

        score = 100

        # Missing value penalty
        missing = int(df.isnull().sum().sum())
        score -= min(missing, 20)

        # Duplicate row penalty
        duplicates = int(df.duplicated().sum())
        score -= duplicates * 5

        # Score should not go below 0
        score = max(score, 0)

        report["data_quality_score"] = score

        return report