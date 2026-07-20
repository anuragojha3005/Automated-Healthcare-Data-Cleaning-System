import json
import os

class CleaningReport:

    def save(self, reports):

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        output_file = os.path.join(OUTPUT_DIR, "cleaning_report.json")

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(reports, f, indent=4)

        print(f"Cleaning report saved to: {output_file}")