import pandas as pd


class MixedTypeDetector:

    def detect(self, df):

        mixed_columns = {}

        for column in df.columns:

            series = df[column].dropna()

            detected_types = set()

            for value in series:

                try:
                    float(value)
                    detected_types.add("Numeric")

                except:
                    detected_types.add("Text")

            if len(detected_types) > 1:

                mixed_columns[column] = list(detected_types)

        return mixed_columns


def datatype_consistency(df):

    inconsistent_columns = {}

    for column in df.columns:

        # Skip text columns
        if df[column].dtype == "object":
            continue

        invalid = df[column].isna().sum()

        inconsistent_columns[column] = {
            "dtype": str(df[column].dtype),
            "missing_values": int(invalid)
        }

    return inconsistent_columns        