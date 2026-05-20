"""Unit tests for SalesProcessor"""

from unittest.mock import MagicMock
from src.analytics import SalesProcessor


def test_sales_processor_init():
    """Test SalesProcessor initialization"""
    mock_spark = MagicMock()
    processor = SalesProcessor(mock_spark, None)
    assert processor.spark is not None
    assert processor.spark == mock_spark


def test_load_sales_data():
    """Test loading sales data"""
    mock_spark = MagicMock()
    mock_df = MagicMock()
    mock_spark.read.option.return_value.option.return_value.csv.return_value = mock_df

    processor = SalesProcessor(mock_spark, None)
    data = processor.load_sales_data("path/to/data.csv")

    assert data is not None
    mock_spark.read.option.assert_called()
    assert data == mock_df
