import pandas as pd
from pathlib import Path
from type_inference import TypeInference


class MetadataExtractor:

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.df = pd.read_csv(file_path)

    def extract(self):
        inference = TypeInference()

        business_types = {}

        for column in self.df.columns:
            business_types[column] = inference.infer(
            column,
            self.df[column]
    )

        metadata = {

            "business_types": business_types,

            "dataset_name": self.file_path.name,

            "rows": int(self.df.shape[0]),

            "columns": int(self.df.shape[1]),

            "column_names": self.df.columns.tolist(),

            "data_types": self.df.dtypes.astype(str).to_dict(),

            "memory_usage_bytes": int(self.df.memory_usage(deep=True).sum()),

            "duplicate_rows": int(self.df.duplicated().sum()),

            "missing_values": self.df.isnull().sum().to_dict()

        }

        return metadata