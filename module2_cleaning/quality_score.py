import pandas as pd


class DataQualityScore:

    def calculate(self, df):

        total_cells = df.shape[0] * df.shape[1]

        if total_cells == 0:
            return 0

        missing = df.isnull().sum().sum()
        duplicates = df.duplicated().sum()

        completeness = (1 - (missing / total_cells)) * 100

        uniqueness = (1 - (duplicates / max(len(df), 1))) * 100

        score = (completeness * 0.7) + (uniqueness * 0.3)

        return round(score, 2)