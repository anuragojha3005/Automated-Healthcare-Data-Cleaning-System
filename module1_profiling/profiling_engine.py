import pandas as pd


class ProfilingEngine:

    def profile(self, df):

        report = {}

        # Missing Values
        report["missing_values"] = df.isnull().sum().to_dict()

        # Missing Percentage
        report["missing_percentage"] = (
            (df.isnull().sum() / len(df)) * 100
        ).round(2).to_dict()

        # Duplicate Rows
        report["duplicate_rows"] = int(df.duplicated().sum())

        # Unique Values
        report["unique_values"] = df.nunique().to_dict()

        # Cardinality
        cardinality = {}

        for column in df.columns:

            unique = df[column].nunique()

            if unique <= 10:
                cardinality[column] = "Low"

            elif unique <= 50:
                cardinality[column] = "Medium"

            else:
                cardinality[column] = "High"

        report["cardinality"] = cardinality

        numeric = df.select_dtypes(include=["number"])

        if not numeric.empty:
            report["statistics"] = numeric.describe().to_dict()
        else:
            report["statistics"] = {}

        return report