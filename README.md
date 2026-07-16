# Healthcare Data Profiling Engine

## Overview
This project is Module 1 of the Automated Healthcare Data Cleaning & Validation System.

It profiles healthcare datasets before cleaning and machine learning by extracting metadata, detecting data quality issues, identifying sensitive information, and generating profiling reports and visualizations.

---

## Features

- Metadata Extraction
- Business Type Inference
- Semantic Detection
- Mixed Type Detection
- Missing Value Analysis
- Duplicate Detection
- Cardinality Analysis
- Correlation Matrix
- Visualization Generation
- Rule Engine
- PII Detection
- JSON Report Generation

---

## Dataset

- patients.csv
- doctors.csv
- appointments.csv
- treatments.csv
- billing.csv

---

## Run

python module1_profiling/profiler.py

---

## Output

outputs/
│
├── profiling/
│      profiling_report.json
│
└── visualizations/
       *.png
