import os
import json
import pandas as pd

from missing_handler import MissingValueHandler
from duplicate_handler import DuplicateHandler
from datatype_handler import DatatypeHandler
from format_handler import FormatHandler
from validation_engine import ValidationEngine
from cleaning_report import CleaningReport
from quality_score import DataQualityScore
from transformation_logger import TransformationLogger
from dashboard_generator import DashboardGenerator


class DataCleaner:

    def __init__(self):

        self.missing = MissingValueHandler()
        self.duplicate = DuplicateHandler()
        self.datatype = DatatypeHandler()
        self.format = FormatHandler()
        self.validation = ValidationEngine()
        self.quality = DataQualityScore()
        self.logger = TransformationLogger()

    def clean_dataset(self, filepath):

        df = pd.read_csv(filepath)

        original_rows = len(df)

        missing_before = df.isnull().sum().sum()
        duplicates_before = df.duplicated().sum()
        quality_before = self.quality.calculate(df)
        quality_after = self.quality.calculate(df)

           # Cleaning Pipeline
        df = self.missing.clean(df)
        df = self.duplicate.clean(df)
        df = self.datatype.clean(df)
        df = self.format.clean(df)

        # Validation (optional)
        validation = self.validation.validate_dataframe(df)

        # Calculate AFTER cleaning
        missing_after = df.isnull().sum().sum()
        duplicates_after = df.duplicated().sum()

        # Transformation Log
        missing_fixed = int(missing_before - missing_after)
        duplicates_removed = int(duplicates_before - duplicates_after)

        if missing_fixed > 0:
               self.logger.add(
                   os.path.basename(filepath),
                   "Missing values filled",
                   missing_fixed
               )

        if duplicates_removed > 0:
               self.logger.add(
                   os.path.basename(filepath),
                   "Duplicate rows removed",
                   duplicates_removed
               )

        report = {
               "dataset": os.path.basename(filepath),
               "original_rows": original_rows,
               "cleaned_rows": len(df),
               "missing_before": int(missing_before),
               "missing_after": int(missing_after),
               "duplicates_before": int(duplicates_before),
               "duplicates_after": int(duplicates_after),
               "quality_before": quality_before,
               "quality_after": quality_after,
               "validation": validation
           }

        return df, report




import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_FOLDER = os.path.join(BASE_DIR, "data", "raw")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "data", "processed")

if __name__ == "__main__":

    # Check if input folder exists
    if not os.path.exists(INPUT_FOLDER):
        print(f"Error: Input folder not found -> {INPUT_FOLDER}")
        exit()

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    reports = []

    cleaner = DataCleaner()

    for file in os.listdir(INPUT_FOLDER):

        if file.endswith(".csv"):

            path = os.path.join(INPUT_FOLDER, file)

            cleaned_df, report = cleaner.clean_dataset(path)

            cleaned_df.to_csv(
                os.path.join(OUTPUT_FOLDER, file),
                index=False
            )

            reports.append(report)

    CleaningReport().save(reports)

    cleaner.logger.save()

    DashboardGenerator().generate(reports)

    print("Cleaning Completed Successfully.")