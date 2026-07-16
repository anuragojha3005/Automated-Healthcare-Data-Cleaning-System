import json

from config import RAW_DATA_DIR, PROFILE_DIR, VISUALIZATION_DIR
from utils import create_directory
from metadata import MetadataExtractor
from visualization import Visualization


def main():

    # Create output folders
    create_directory(PROFILE_DIR)
    create_directory(VISUALIZATION_DIR)

    print("=" * 50)
    print("Healthcare Data Profiling Engine")
    print("=" * 50)

    profiling_report = {}

    csv_files = RAW_DATA_DIR.glob("*.csv")

    for file in csv_files:

        print(f"Processing : {file.name}")

        extractor = MetadataExtractor(file)

        visual = Visualization()

        df = extractor.df

        # Generate Missing Heatmap
        visual.missing_heatmap(
            df,
            VISUALIZATION_DIR / f"{file.stem}_missing.png"
        )

        # Generate Correlation Heatmap
        visual.correlation_heatmap(
            df,
            VISUALIZATION_DIR / f"{file.stem}_correlation.png"
        )

        # Generate Outlier Plot
        visual.outlier_plot(
            df,
            VISUALIZATION_DIR
        )

        # Generate Metadata Report
        profiling_report[file.stem] = extractor.extract()

    output_file = PROFILE_DIR / "profiling_report.json"

    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(profiling_report, json_file, indent=4)

    print("\nProfiling Report Generated Successfully.")
    print(f"Saved at : {output_file}")


if __name__ == "__main__":
    main()