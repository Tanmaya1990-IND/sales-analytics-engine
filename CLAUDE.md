# Claude.md - Sales Analytics Engine Documentation

## 1. Project Overview

**Project Name:** PySpark Sales Analytics Engine

**Purpose:** A distributed data processing engine for ETL (Extract, Transform, Load) and business intelligence on sales data using Apache Spark.

**Key Capabilities:**
- Load and validate sales data from multiple sources
- Transform and clean data with quality checks
- Aggregate sales metrics by region, product, and time period
- Generate actionable business insights and reports
- Support for batch processing at scale

**Target Users:** Data engineers, analysts, and business intelligence teams

**Current Status:** Initial implementation with core ETL pipeline ready for local development and testing

---

## 2. Architecture

### High-Level Pipeline

```
Input Data (CSV/Database)
    ↓
DataIngestion (Load)
    ↓
DataTransformation (Clean & Standardize)
    ↓
DataValidation (Quality Checks)
    ↓
SalesProcessor (Business Logic)
    ↓
Aggregations (Metrics & Analytics)
    ↓
Output (CSV/Database/Reports)
```

### Core Components

**src/main.py**
- Entry point for the application
- Orchestrates the complete ETL pipeline
- Manages Spark session lifecycle

**src/analytics/**
- `sales_processor.py` - Sales data processing with business rules
- `aggregations.py` - Group-by aggregations and rollups
- `metrics.py` - Advanced metrics with window functions

**src/config.py**
- Environment-based configuration (development/production)
- Database connection settings
- Spark optimization parameters

**src/logger.py**
- Centralized logging with console and file output
- Structured logging for monitoring

### Planned Three-Processor Architecture

```
┌─────────────────────────────────────┐
│   SalesProcessor                    │
│   - Load sales transactions         │
│   - Apply business rules            │
│   - Detect anomalies                │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│   CustomerProcessor (Planned)       │
│   - Customer master data            │
│   - Segmentation (High/Med/Low)    │
│   - Churn risk analysis             │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│   InventoryProcessor (Planned)      │
│   - Stock levels                    │
│   - Turnover rates                  │
│   - Stockout forecasting            │
└─────────────────────────────────────┘
```

---

## 3. Technology Stack

**Core:**
- PySpark 3.5.8 (or compatible version)
- Python 3.8+
- Java 8+ (required by Spark)

**Data Processing:**
- pandas >= 3.0.0 (for local operations)
- numpy (transitively from pandas)

**Testing & Quality:**
- pytest >= 7.4.0 (unit testing)
- pytest-cov >= 4.1.0 (coverage reporting)

**Configuration & Utilities:**
- python-dotenv >= 1.0.0 (environment variables)
- psycopg2-binary (PostgreSQL adapter - optional)

**Development Environment:**
- Windows 11, Python 3.14
- Git for version control
- Local Spark (no Hadoop required for development)

**Deployment Targets (Future):**
- Apache Hadoop cluster (for production)
- Cloud Spark services (Databricks, AWS EMR, Azure Synapse)
- PostgreSQL database (optional data store)

---

## 4. Naming Conventions

### Classes
- **Format:** PascalCase
- **Examples:** `SalesProcessor`, `DataValidator`, `Aggregations`
- **Rule:** One public class per module (typically)

### Functions & Methods
- **Format:** snake_case
- **Examples:** `load_sales_data()`, `process_sales()`, `calculate_metrics()`
- **Rule:** Use descriptive action verbs (load, process, validate, calculate)

### Variables & Parameters
- **Format:** snake_case
- **Examples:** `sales_df`, `config_obj`, `record_count`
- **Rule:** Use meaningful names, avoid single letters except in loops

### Constants
- **Format:** UPPER_SNAKE_CASE
- **Examples:** `DEFAULT_BATCH_SIZE`, `MAX_PARTITION_COUNT`
- **Scope:** Module-level or class-level constants

### Private Methods/Variables
- **Format:** Prefix with underscore
- **Examples:** `_validate_schema()`, `_internal_state`
- **Rule:** Not intended for external use

### File Names
- **Format:** snake_case.py
- **Examples:** `sales_processor.py`, `config.py`
- **Rule:** Match the main class name (lowercased)

---

## 5. Coding Standards

### PEP 8 Compliance
- Line length: 100 characters (practical limit, 79 is ideal)
- Indentation: 4 spaces (never tabs)
- Two blank lines between top-level definitions
- One blank line between method definitions

### Type Hints
**Mandatory on all functions:**
```python
def load_sales_data(self, path: str) -> DataFrame:
    """Load sales data from a given path"""
    pass

def calculate_metrics(
    self,
    data: DataFrame,
    metrics: List[str]
) -> Dict[str, float]:
    """Calculate multiple metrics"""
    pass
```

### Docstrings
**Format:** Google-style docstrings for all public classes and methods

```python
def process(self, data: DataFrame) -> DataFrame:
    """Process sales data and prepare it for analysis.
    
    Applies data cleaning, type conversions, and business rules
    to the input DataFrame.
    
    Args:
        data: Input DataFrame with raw sales data
        
    Returns:
        Processed DataFrame with cleaned and validated data
        
    Raises:
        ValueError: If input data schema is invalid
        ProcessingError: If processing fails
    """
    pass
```

### Import Organization
```python
# Standard library imports
import os
from typing import List, Dict, Optional

# Third-party imports
from pyspark.sql import SparkSession, DataFrame

# Local imports
from src.config import get_config
from src.logger import setup_logger
```

### Error Handling
- Use specific exception types (not bare `Exception`)
- Include context in error messages
- Log errors before raising

```python
try:
    spark = SparkSession.builder.getOrCreate()
except Exception as e:
    logger.error(f"Failed to create Spark session: {e}")
    raise ProcessingError(f"Spark initialization failed: {e}")
```

### Comments
- Minimal comments - code should be self-documenting
- Comments should explain WHY, not WHAT
- No commented-out code (use git history instead)

---

## 6. Data Standards

### Dates
- **Format:** ISO 8601 (YYYY-MM-DD)
- **Type:** DateType in Spark (not StringType)
- **Timezone:** UTC preferred, specify if different
- **Example:** `2024-01-15`

### Currency & Amounts
- **Decimal Places:** Exactly 2 (e.g., 1000.00, not 1000)
- **Type:** DecimalType(10,2) in Spark
- **Format:** No currency symbols in data (metadata only)
- **Example:** `1500.75`

### Validation Rules

**Email Addresses:**
```python
import re
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
```

**Phone Numbers:**
```python
# Format: +1234567890 or (123) 456-7890
phone_pattern = r'^(\+\d{1,3})?[\s.-]?\(?(\d{3})\)?[\s.-]?(\d{3})[\s.-]?(\d{4})$'
```

**Required Fields:** All critical columns should be NOT NULL
- sales.amount, sales.customer_id, sales.product_id
- customer.email must be valid if present
- inventory.product_id (NOT NULL)

### Data Quality Checks
- No null values in required columns
- Amounts > 0 (for sales)
- Dates within reasonable range (e.g., last 10 years)
- Text fields trimmed of whitespace
- Email addresses properly formatted

---

## 7. Testing Requirements

### Coverage Minimum
- **Target:** 80% code coverage
- **Tool:** pytest with pytest-cov
- **Calculation:** Includes unit tests only (not integration tests)

### Test Types

**Unit Tests (tests/unit/)**
- Test individual functions and classes in isolation
- Use mocks for Spark sessions when possible
- File pattern: `test_*.py`
- Fast execution (< 1 second per test)

**Integration Tests (tests/integration/)**
- Test end-to-end workflows with real Spark
- Use sample data or fixtures
- Reserved for validation of complete pipelines
- May be skipped in local development (marked with `@pytest.mark.skip`)

### Test Structure
```python
def test_sales_processor_initialization():
    """Test SalesProcessor initializes with valid config"""
    mock_spark = MagicMock()
    processor = SalesProcessor(mock_spark, config)
    assert processor.spark is not None

@pytest.mark.skip(reason="Requires Spark context")
def test_aggregations_by_region():
    """Integration test - aggregate sales by region"""
    pass
```

### Running Tests
```bash
# Run all tests with coverage
pytest tests/ -v --cov=src --cov-report=html

# Run only unit tests
pytest tests/unit/ -v

# Run specific test file
pytest tests/unit/test_sales_processor.py -v
```

---

## 8. Common Patterns

### Spark DataFrame Operations

**Load CSV with Schema Inference:**
```python
def load_sales_data(self, path: str) -> DataFrame:
    """Load CSV with automatic schema inference"""
    return self.spark.read.option("header", "true").option(
        "inferSchema", "true"
    ).csv(path)
```

**Aggregation with GroupBy:**
```python
def by_region(df: DataFrame) -> DataFrame:
    """Group sales by region and sum amounts"""
    return df.groupBy("region").agg(
        F.sum("amount").alias("total_sales"),
        F.count("*").alias("transaction_count")
    )
```

**Window Functions for Running Totals:**
```python
from pyspark.sql.window import Window

def calculate_running_total(
    df: DataFrame,
    partition_col: str,
    order_col: str
) -> DataFrame:
    """Calculate running total within partitions"""
    window_spec = Window.partitionBy(
        partition_col
    ).orderBy(order_col)
    
    return df.withColumn(
        "running_total",
        F.sum("amount").over(window_spec)
    )
```

**Data Filtering & Transformation:**
```python
def clean_data(df: DataFrame) -> DataFrame:
    """Remove duplicates and handle nulls"""
    return df.dropDuplicates() \
        .dropna(subset=["customer_id", "amount"]) \
        .filter(F.col("amount") > 0)
```

### Configuration Management

**Development Config:**
```python
config = get_config("development")
# Results in: DEBUG=True, SPARK_MASTER="local[*]"
```

**Production Config:**
```python
config = get_config("production")
# Results in: DEBUG=False, SPARK_MASTER from env variable
```

### Logging Pattern

```python
from src.logger import setup_logger

logger = setup_logger(__name__)

def process_data(data: DataFrame) -> DataFrame:
    logger.info("Starting data processing")
    try:
        cleaned = clean_data(data)
        logger.info(f"Cleaned {cleaned.count()} records")
        return cleaned
    except Exception as e:
        logger.error(f"Processing failed: {e}", exc_info=True)
        raise
```

---

## 9. Error Handling & Logging

### Error Hierarchy

**Custom Exceptions:**
```python
class AnalyticsError(Exception):
    """Base exception for analytics engine"""
    pass

class DataIngestionError(AnalyticsError):
    """Raised when data loading fails"""
    pass

class ValidationError(AnalyticsError):
    """Raised when data validation fails"""
    pass

class ProcessingError(AnalyticsError):
    """Raised when data processing fails"""
    pass
```

### Error Handling Pattern

```python
try:
    processor = SalesProcessor(spark, config)
    data = processor.load_sales_data(path)
    result = processor.process(data)
except ValidationError as e:
    logger.error(f"Data validation failed: {e}")
    raise  # Re-raise for caller to handle
except ProcessingError as e:
    logger.error(f"Processing error: {e}")
    raise
except Exception as e:
    logger.error(f"Unexpected error: {e}", exc_info=True)
    raise ProcessingError(f"Unexpected failure: {e}")
finally:
    spark.stop()
```

### Logging Levels

**INFO:** User-facing information
- Engine startup/shutdown
- Data loaded/processed counts
- Execution milestones

**WARNING:** Potentially problematic situations
- Falling back to defaults
- Skipped records
- Performance concerns

**ERROR:** Errors that prevent processing
- Failed to load data
- Invalid configurations
- Processing failures

**DEBUG:** Detailed diagnostic information (development only)
- Variable values
- Intermediate results
- Function entry/exit

### Logging Format

```python
logger.info(f"Loaded {count} records from {path}")
logger.error(f"Failed to process {failed_count} records: {error}")
logger.warning(f"Using default config: {default_value}")
```

---

## 10. Example Code Patterns

### Complete Sales Processor Example

```python
"""Sales data processor for analytics."""

from typing import Tuple
from pyspark.sql import SparkSession, DataFrame

from src.logger import setup_logger

logger = setup_logger(__name__)


class SalesProcessor:
    """Process sales data and prepare it for analysis."""

    def __init__(self, spark: SparkSession, config):
        """Initialize with Spark session and config.
        
        Args:
            spark: SparkSession instance
            config: Configuration object
        """
        self.spark = spark
        self.config = config
        logger.info("SalesProcessor initialized")

    def load_sales_data(self, path: str) -> DataFrame:
        """Load sales data from CSV.
        
        Args:
            path: Path to CSV file
            
        Returns:
            DataFrame with loaded data
            
        Raises:
            DataIngestionError: If file not found or invalid
        """
        logger.info(f"Loading sales data from {path}")
        try:
            return self.spark.read.option("header", "true").option(
                "inferSchema", "true"
            ).csv(path)
        except Exception as e:
            logger.error(f"Failed to load data: {e}")
            raise DataIngestionError(f"Failed to load {path}: {e}")

    def process(self, data: DataFrame) -> DataFrame:
        """Process sales data.
        
        Args:
            data: Input DataFrame
            
        Returns:
            Processed DataFrame
        """
        logger.info("Processing sales data")
        return data
```

### Configuration Usage Example

```python
from src.config import get_config
from src.logger import setup_logger
from pyspark.sql import SparkSession

# Get environment-based configuration
config = get_config()

# Initialize logging
logger = setup_logger(__name__)
logger.info(f"Debug mode: {config.DEBUG}")

# Create Spark session with config
spark = SparkSession.builder.appName(
    config.SPARK_APP_NAME
).master(config.SPARK_MASTER).getOrCreate()

# Use configuration paths
input_path = f"{config.DATA_PATH}/raw/sales.csv"
output_path = f"{config.OUTPUT_PATH}/results.csv"
```

### Testing Pattern with Mocks

```python
from unittest.mock import MagicMock
from src.analytics import SalesProcessor


def test_sales_processor_init():
    """Test SalesProcessor initialization."""
    mock_spark = MagicMock()
    config = {"DEBUG": True}
    
    processor = SalesProcessor(mock_spark, config)
    
    assert processor.spark == mock_spark
    assert processor.config == config


def test_load_sales_data():
    """Test loading sales data."""
    mock_spark = MagicMock()
    mock_df = MagicMock()
    mock_spark.read.option.return_value.option.return_value.csv.return_value = mock_df
    
    processor = SalesProcessor(mock_spark, None)
    result = processor.load_sales_data("path/to/file.csv")
    
    assert result == mock_df
    mock_spark.read.option.assert_called()
```

---

## 11. Development Workflow

### Setting Up Locally

```bash
# Clone repository
git clone https://github.com/Tanmaya1990-IND/sales-analytics-engine.git
cd sales-analytics-engine

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m src.main

# Run tests
pytest tests/ -v --cov=src
```

### Making Changes

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make changes following conventions above
3. Write tests for new functionality
4. Run tests: `pytest tests/ -v`
5. Commit with clear message: `git commit -m "Add description"`
6. Push and create pull request

### Batch File Runners

```batch
# Windows: Double-click run.bat to execute
# Windows: Double-click run_tests.bat to run tests
```

---

## 12. Quick Reference

| Item | Standard |
|------|----------|
| **Class Names** | PascalCase |
| **Functions** | snake_case |
| **Constants** | UPPER_SNAKE_CASE |
| **Line Length** | 100 characters |
| **Indentation** | 4 spaces |
| **Type Hints** | Required on all functions |
| **Docstrings** | Google-style |
| **Test Coverage** | Minimum 80% |
| **Date Format** | ISO 8601 (YYYY-MM-DD) |
| **Decimal Places** | 2 (for currency) |
| **Branch Name** | main (default) |

---

## 13. Important Notes

- **Spark Warnings on Windows:** Hadoop warnings are expected without full Hadoop installation. These don't affect local development.
- **File Writing:** Use Python CSV module instead of Spark for local output on Windows to avoid permission issues.
- **Testing:** Some integration tests are skipped locally due to Spark context issues on Windows. Run on Linux/Mac or Docker for full integration testing.
- **Database:** PostgreSQL adapter (psycopg2) is optional. Install only if using PostgreSQL backend.

---

**Document Version:** 1.0  
**Last Updated:** May 20, 2026  
**Maintainer:** Data Engineering Team
