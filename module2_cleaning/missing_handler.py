import pandas as pd
from pandas.api.types import is_numeric_dtype


class MissingValueHandler:

    def clean(self, df):

        df = df.copy()

        for column in df.columns:

            # Numeric columns
            if is_numeric_dtype(df[column]):

                median = df[column].median()

                if pd.notna(median):
                    df[column] = df[column].fillna(median)

            # Non-numeric columns
            else:

                mode = df[column].mode()

                if not mode.empty:
                    df[column] = df[column].fillna(mode.iloc[0])
                else:
                    df[column] = df[column].fillna("Unknown")

        return df