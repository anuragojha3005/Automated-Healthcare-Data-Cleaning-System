import os
import pandas as pd


class DashboardGenerator:

    def generate(self, reports):

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        output_file = os.path.join(
            BASE_DIR,
            "outputs",
            "dashboard_summary.csv"
        )

        df = pd.DataFrame(reports)

        df.to_csv(output_file, index=False)

        print("Dashboard Summary Generated.")