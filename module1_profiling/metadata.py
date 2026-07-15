import pandas as pd
from pathlib import Path

from type_inference import TypeInference
from semantic_detector import SemanticDetector, detect_pii

from mixed_type_detector import MixedTypeDetector
from mixed_type_detector import datatype_consistency

from profiling_engine import ProfilingEngine


class MetadataExtractor:

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.df = pd.read_csv(file_path)

    def extract(self):

        # Business Type Inference
        inference = TypeInference()

        business_types = {}

        for column in self.df.columns:
            business_types[column] = inference.infer(
                column,
                self.df[column]
            )

        # Semantic Detection
        semantic = SemanticDetector()

        semantic_meaning = {}

        pii_columns = []

        for column in self.df.columns:

            semantic_meaning[column] = semantic.detect(column)

            if detect_pii(column):
                pii_columns.append(column)

        # Mixed Type Detector
        mixed_detector = MixedTypeDetector()

        mixed_columns = mixed_detector.detect(self.df)        

        consistency = datatype_consistency(self.df)

        engine = ProfilingEngine()

        profile = engine.profile(self.df)

        metadata = {

            "dataset_name": self.file_path.name,

            "rows": int(self.df.shape[0]),

            "columns": int(self.df.shape[1]),

            "column_names": self.df.columns.tolist(),

            "data_types": self.df.dtypes.astype(str).to_dict(),

            "business_types": business_types,

            "semantic_meaning": semantic_meaning,

            "pii_columns": pii_columns,

            "mixed_columns": mixed_columns,

            "datatype_consistency": consistency,
            
            "profile": profile,

            "memory_usage_bytes": int(self.df.memory_usage(deep=True).sum()),

            "duplicate_rows": int(self.df.duplicated().sum()),

            "missing_values": self.df.isnull().sum().to_dict()

        }


        print("DEBUG")
        print(metadata)

        return metadata