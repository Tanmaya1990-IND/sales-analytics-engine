# Sales Analytics Engine - Quick Start Guide

## Running the Application

### Option 1: Using Batch Files (Easiest)

**Run the Analytics Engine:**
```bash
Double-click: run.bat
```

**Run Unit Tests:**
```bash
Double-click: run_tests.bat
```

### Option 2: Using Command Line

**Run the Analytics Engine:**
```powershell
C:\Users\misra\AppData\Local\Python\bin\python.exe -m src.main
```

**Run Tests:**
```powershell
C:\Users\misra\AppData\Local\Python\bin\python.exe -m pytest tests/ -v
```

## What the Engine Does

When you run `run.bat`, the Sales Analytics Engine will:

1. **Initialize** - Starts Spark session in local mode
2. **Create Sample Data** - Generates 9 test records (2024-01-01 to 2024-01-03)
3. **Load Data** - Reads CSV file from `./data/raw/sales_sample.csv`
4. **Validate** - Checks schema (date, product, region, amount)
5. **Process** - Executes data transformations
6. **Display Results** - Shows first 5 rows in formatted table
7. **Summary** - Displays execution metrics

## Output Directories

After running the script, you'll see:

```
sales-analytics-engine/
├── data/
│   ├── raw/
│   │   └── sales_sample.csv          # Generated sample data
│   └── outputs/
│       └── processed_sales.csv       # Processed results (if saved)
└── logs/                             # Log files (optional)
```

## Sample Data

The script creates this test data:

| date       | product    | region | amount  |
|-----------|-----------|--------|---------|
| 2024-01-01 | Product A | North  | 1000.00 |
| 2024-01-01 | Product B | South  | 1500.00 |
| 2024-01-01 | Product A | East   | 800.00  |
| 2024-01-02 | Product C | West   | 2000.00 |
| 2024-01-02 | Product A | North  | 1200.00 |
| 2024-01-02 | Product B | South  | 1800.00 |
| 2024-01-03 | Product B | East   | 950.00  |
| 2024-01-03 | Product C | North  | 2200.00 |
| 2024-01-03 | Product A | West   | 1100.00 |

## Expected Output

```
========================================
Sales Analytics Engine
========================================

Starting Sales Analytics Engine (DEBUG: True)
Environment: development
Sales processor initialized successfully
Creating sample sales data
Sample data saved to ./data/raw/sales_sample.csv
Loading sales data
Loaded 9 records

Data Schema:
root
 |-- date: date (nullable = true)
 |-- product: string (nullable = true)
 |-- region: string (nullable = true)
 |-- amount: double (nullable = true)

Processing data

Sample data (first 5 rows):
+----------+---------+------+------+
|date      |product  |region|amount|
+----------+---------+------+------+
|2024-01-01|Product A|North |1000.0|
|2024-01-01|Product B|South |1500.0|
|2024-01-01|Product A|East  |800.0 |
|2024-01-02|Product C|West  |2000.0|
|2024-01-02|Product A|North |1200.0|
+----------+---------+------+------+

Total records processed: 9

==================================================
EXECUTION SUMMARY
==================================================
Input file: ./data/raw/sales_sample.csv
Output directory: ./data/outputs
Records processed: 9
Status: Completed successfully [OK]
==================================================

Spark session stopped
```

## Troubleshooting

### Issue: "Python.exe not found"
**Solution:** The batch files use the correct Python path. Just double-click `run.bat`

### Issue: "Permission denied" for output
**Solution:** This is normal on Windows. The core functionality still works - data is processed successfully.

### Issue: Hadoop warnings
**Solution:** These warnings are expected on Windows without Hadoop installed. They don't affect local testing.

## Project Structure

```
sales-analytics-engine/
├── src/
│   ├── main.py                      # Entry point
│   ├── config.py                    # Configuration
│   ├── logger.py                    # Logging setup
│   └── analytics/
│       ├── sales_processor.py       # Data processing
│       ├── aggregations.py          # Aggregation functions
│       └── metrics.py               # Metrics calculations
├── tests/
│   ├── unit/                        # Unit tests
│   └── conftest.py                  # Test configuration
├── data/
│   ├── raw/                         # Input data
│   └── outputs/                     # Results
├── run.bat                          # Run application
├── run_tests.bat                    # Run tests
└── QUICKSTART.md                    # This file
```

## Next Steps

1. **Run the Application** - Double-click `run.bat`
2. **Run Tests** - Double-click `run_tests.bat`
3. **Add Your Data** - Place CSV files in `./data/raw/`
4. **Modify Processing** - Edit `src/analytics/sales_processor.py`
5. **Create Aggregations** - Implement in `src/analytics/aggregations.py`

## Requirements

- Python 3.8+
- PySpark 3.5.8+
- Dependencies: pandas, pytest, python-dotenv

All dependencies are already installed!

---

**Created:** 2026-05-20
**Project:** PySpark Sales Analytics Engine
**Environment:** Windows 11 + Python 3.14
