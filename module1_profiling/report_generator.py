import json


class ReportGenerator:

    def save(self, report, output_file):

        with open(output_file, "w", encoding="utf-8") as file:

            json.dump(
                report,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("Report Saved Successfully")