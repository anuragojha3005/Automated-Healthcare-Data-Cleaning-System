import pandas as pd


class TypeInference:

    def infer(self, column_name, series):

        column = column_name.lower()

        # Identifier
        if column.endswith("_id") or column == "id":
            return "Identifier"

        # Email
        if "email" in column:
            return "Email"

        # Phone
        if "phone" in column or "contact" in column:
            return "Phone"

        # Date
        if "date" in column or "dob" in column:
            return "Date"

        # Name
        if "name" in column:
            return "Name"

        # Address
        if "address" in column:
            return "Address"

        # Insurance
        if "insurance" in column:
            return "Insurance"

        # Cost / Amount
        if "cost" in column or "amount" in column:
            return "Numeric"

        # Numeric columns
        if pd.api.types.is_numeric_dtype(series):
            return "Numeric"

        # Categorical
        if series.nunique() <= 20:
            return "Category"

        # Default
        return "Text"