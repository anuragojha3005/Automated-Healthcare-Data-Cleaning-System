# Module 2: Automated Data Cleaning & Validation System

## Overview

Module 2 is responsible for automatically cleaning, validating, and improving the quality of healthcare datasets generated after the profiling stage (Module 1).

The module reads raw CSV files, applies multiple data cleaning operations, validates important fields, calculates data quality metrics, and generates cleaned datasets along with detailed reports.

---

# Objectives

- Clean missing values
- Remove duplicate records
- Standardize data formats
- Validate important fields
- Generate cleaned datasets
- Produce cleaning reports
- Calculate data quality scores
- Maintain transformation logs

---

# Project Structure

```
module2_cleaning/

│── cleaner.py
│── missing_handler.py
│── duplicate_handler.py
│── datatype_handler.py
│── format_handler.py
│── validation_engine.py
│── rules.py
│── quality_score.py
│── cleaning_report.py
│── transformation_logger.py
│── dashboard_generator.py
```

---

# Workflow

```
Raw Dataset
      │
      ▼
Missing Value Handler
      │
      ▼
Duplicate Handler
      │
      ▼
Datatype Conversion
      │
      ▼
Format Standardization
      │
      ▼
Validation Engine
      │
      ▼
Quality Score
      │
      ▼
Transformation Logger
      │
      ▼
Cleaned Dataset
```

---

# Features

## Missing Value Handling

- Numeric columns
  - Replace missing values using Median

- Categorical columns
  - Replace missing values using Mode

---

## Duplicate Removal

- Detect duplicate records
- Remove duplicate rows

---

## Datatype Conversion

Automatically converts:

- Date columns
- Datetime columns
- Numeric columns

---

## Text Formatting

Standardizes text fields by

- Removing extra spaces
- Trimming values
- Standardizing string formatting

---

## Validation Engine

Performs validation for

- Email addresses
- Phone numbers
- Age values
- Positive billing amounts
- Cost fields

---

## Data Quality Score

Calculates

- Completeness
- Uniqueness

Returns a quality score between **0 and 100**.

---

## Transformation Logger

Records every cleaning operation including

- Missing values filled
- Duplicate rows removed
- Number of affected records

---

# Input

```
data/raw/

patients.csv

doctors.csv

appointments.csv

treatments.csv

billing.csv
```

---

# Output

```
data/processed/

patients.csv

doctors.csv

appointments.csv

treatments.csv

billing.csv
```

Reports

```
outputs/

cleaning_report.json

transformation_log.json

dashboard_summary.csv
```

---

# Cleaning Report Example

```json
{
    "dataset": "patients.csv",
    "original_rows": 200,
    "cleaned_rows": 198,
    "missing_before": 18,
    "missing_after": 0,
    "duplicates_before": 2,
    "duplicates_after": 0,
    "quality_before": 84.3,
    "quality_after": 99.8
}
```

---

# Validation Rules

| Field | Rule |
|---------|------|
| Email | Valid Email Format |
| Phone | 10 Digit Number |
| Age | 0–120 |
| Amount | Positive Value |
| Cost | Positive Value |

---

# Technologies Used

- Python 3.11
- Pandas
- NumPy
- JSON
- Regular Expressions
- OS Module

---

# Installation

```bash
git clone <repository-url>

cd Automated-Healthcare-Data-Cleaning-System

pip install -r requirements.txt
```

---

# Run

```bash
python module2_cleaning/cleaner.py
```

---

# Generated Outputs

- Cleaned CSV Files
- Cleaning Report
- Transformation Log
- Dashboard Summary CSV

---

# Future Enhancements

- Outlier Detection
- Data Drift Detection
- Automated Rule Configuration
- Cross-table Validation
- Schema Validation
- PDF Report Generation
- HTML Dashboard
- Power BI Integration

---

# Module Status

| Component | Status |
|------------|--------|
| Missing Value Handler | ✅ |
| Duplicate Removal | ✅ |
| Datatype Conversion | ✅ |
| Format Standardization | ✅ |
| Validation Engine | ✅ |
| Quality Score | ✅ |
| Cleaning Report | ✅ |
| Transformation Logger | ✅ |
| Dashboard Summary | ✅ |

---
