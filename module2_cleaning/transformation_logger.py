import json
import os

class TransformationLogger:

    def __init__(self):
        self.logs = []

    def add(self, dataset, operation, affected_rows):
        self.logs.append({
            "dataset": dataset,
            "operation": operation,
            "affected_rows": affected_rows
        })

    def save(self):

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        OUTPUT_DIR = os.path.join(BASE_DIR, "outputs",)

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        output_file = os.path.join(OUTPUT_DIR, "transformation_log.json")

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(self.logs, f, indent=4)

        print("Transformation Log Saved Successfully.")