# Module 1: Advanced Data Profiling & Metadata Intelligence

## Overview

Module 1 is the first stage of the **Automated Healthcare Data Cleaning & Validation System**. It performs comprehensive profiling of healthcare datasets to understand their structure, identify data quality issues, detect sensitive information, and generate metadata reports before any cleaning or transformation is applied.

The generated profiling report serves as the input for the automated cleaning pipeline in Module 2.

---

## Objectives

- Analyze dataset structure
- Extract dataset metadata
- Infer business data types
- Detect semantic meaning of columns
- Identify Personally Identifiable Information (PII)
- Detect missing values and duplicates
- Analyze column cardinality
- Check data type consistency
- Generate profiling reports
- Create data quality visualizations

---

## Features

### Metadata Extraction
- Dataset name
- Number of rows
- Number of columns
- Column names
- Data types
- Memory usage

### Type Inference
Automatically identifies column types such as:
- Integer
- Float
- Date
- String
- Boolean

### Semantic Detection
Recognizes business meaning of columns including:
- Patient ID
- Doctor ID
- Appointment ID
- Name
- Email
- Phone Number
- Address
- Billing Amount

### PII Detection
Detects sensitive columns such as:
- Patient Name
- Email Address
- Phone Number
- Address

### Data Quality Analysis
- Missing Value Analysis
- Duplicate Detection
- Cardinality Analysis
- Data Type Consistency
- Mixed Type Detection

### Rule Engine
Identifies:
- Missing values
- Duplicate records
- Invalid data types
- Potential PII fields
- Suspicious columns

### Visualization
Automatically generates:
- Missing Value Heatmap
- Correlation Heatmap
- Outlier Distribution

### Report Generation
Creates a detailed JSON profiling report for every dataset.

---

## Project Structure

```
module1_profiling/

├── profiler.py
├── metadata.py
├── type_inference.py
├── semantic_detector.py
├── mixed_type_detector.py
├── profiling_engine.py
├── visualization.py
├── rule_engine.py
├── report_generator.py
├── config.py
└── utils.py
```

---

## Input

```
data/raw/

patients.csv

doctors.csv

appointments.csv

treatments.csv

billing.csv
```

---

## Output

```
outputs/

profiling/

    profiling_report.json

visualizations/

    missing_heatmap.png

    correlation_heatmap.png

    outlier_plot.png
```

---

## Workflow

```
Healthcare Dataset
        │
        ▼
Metadata Extraction
        │
        ▼
Type Inference
        │
        ▼
Semantic Detection
        │
        ▼
PII Detection
        │
        ▼
Profiling Engine
        │
        ▼
Rule Engine
        │
        ▼
Visualizations
        │
        ▼
Profiling Report
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Missingno
- JSON
- Regular Expressions (Regex)

---

## Run Module

```bash
python module1_profiling/profiler.py
```

---

## Generated Outputs

- Metadata Report
- Profiling Report (JSON)
- Missing Value Analysis
- Duplicate Analysis
- Correlation Matrix
- Outlier Detection
- Data Quality Summary
- Visualizations

---

## Future Improvements

- Statistical Profiling
- Data Drift Detection
- Schema Validation
- Custom Rule Configuration
- Automated Alerts
- HTML Profiling Report

---

## Module Status

| Feature | Status |
|---------|--------|
| Metadata Extraction | ✅ |
| Type Inference | ✅ |
| Semantic Detection | ✅ |
| PII Detection | ✅ |
| Missing Value Analysis | ✅ |
| Duplicate Detection | ✅ |
| Rule Engine | ✅ |
| Profiling Report | ✅ |
| Visualization | ✅ |
