class FormatHandler:

    def clean(self, df):

        for column in df.select_dtypes(include="object"):

            df[column] = (
                df[column]
                .astype(str)
                .str.strip()
            )

        return df