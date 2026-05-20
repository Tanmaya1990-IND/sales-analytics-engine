# Sales Analytics Engine

A PySpark-based analytics engine for processing and analyzing sales data.

## Project Structure

```
sales-analytics-engine/
├── src/
│   ├── __init__.py
│   ├── config.py          # Configuration management
│   ├── logger.py          # Logging setup
│   ├── main.py            # Entry point
│   └── analytics/
│       ├── __init__.py
│       ├── sales_processor.py    # Data loading and processing
│       ├── aggregations.py       # Aggregation functions
│       └── metrics.py            # Metrics calculations
├── tests/
│   ├── __init__.py
│   ├── conftest.py        # Shared fixtures
│   ├── unit/              # Unit tests
│   └── integration/       # Integration tests
├── data/
│   ├── raw/               # Original data
│   ├── processed/         # Transformed data
│   └── outputs/           # Results
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

```bash
pip install -e .
```

## Development Setup

```bash
pip install -e ".[dev]"
```

## Running Tests

```bash
pytest tests/
```

## Running the Engine

```bash
python -m src.main
```

## Configuration

Set environment variables to configure the engine:

- `ENV`: Environment (development/production, default: development)
- `SPARK_APP_NAME`: Spark application name
- `DATA_PATH`: Path to input data
- `OUTPUT_PATH`: Path for output results
- `DEBUG`: Enable debug mode (true/false)

## Usage

```python
from src.analytics import SalesProcessor, Aggregations, Metrics
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Analytics").getOrCreate()
processor = SalesProcessor(spark, config)

# Load and process data
sales_data = processor.load_sales_data("path/to/data.csv")
processed_data = processor.process(sales_data)

# Perform aggregations
regional_sales = Aggregations.by_region(processed_data)
```
