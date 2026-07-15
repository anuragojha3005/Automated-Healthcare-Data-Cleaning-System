from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"

OUTPUT_DIR = BASE_DIR / "outputs"

PROFILE_DIR = OUTPUT_DIR / "profiling"

VISUALIZATION_DIR = OUTPUT_DIR / "visualizations"