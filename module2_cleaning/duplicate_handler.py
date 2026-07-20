class DuplicateHandler:

    def clean(self, df):

        return df.drop_duplicates()