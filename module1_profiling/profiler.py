from config import PROFILE_DIR, VISUALIZATION_DIR
from utils import create_directory

def main():
    create_directory(PROFILE_DIR)
    create_directory(VISUALIZATION_DIR)

    print("====================================")
    print("Healthcare Data Profiling Engine")
    print("Module 1 Started Successfully")
    print("====================================")

if __name__ == "__main__":
    main()