import pandas as pd


class DatatypeHandler:

    def clean(self, df):

        for column in df.columns:

            if "date" in column.lower():

                df[column] = pd.to_datetime(
                    df[column],
                    errors="coerce"
                )

        return df