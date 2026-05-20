"""Shared fixtures and configuration for tests"""

import pytest
from unittest.mock import Mock, MagicMock


@pytest.fixture(scope="session")
def spark_session():
    """Create a mock Spark session for testing"""
    spark = MagicMock()
    spark.createDataFrame = MagicMock(return_value=MagicMock())
    return spark


@pytest.fixture
def sample_sales_data(spark_session):
    """Create sample sales data for testing"""
    data = [
        ("2024-01-01", "Product A", "Region 1", 1000.0),
        ("2024-01-02", "Product B", "Region 2", 1500.0),
        ("2024-01-03", "Product A", "Region 1", 1200.0),
    ]

    mock_df = MagicMock()
    mock_df.count.return_value = len(data)
    mock_df.columns = ["date", "product", "region", "amount"]
    return mock_df
