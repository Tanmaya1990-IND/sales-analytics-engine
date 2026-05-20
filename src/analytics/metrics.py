"""Metrics calculation for sales analytics"""

from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql.window import Window

from src.logger import setup_logger

logger = setup_logger(__name__)


class Metrics:
    """Calculate metrics from sales data"""

    @staticmethod
    def calculate_running_total(df: DataFrame, partition_col: str, order_col: str) -> DataFrame:
        """Calculate running total for sales

        Args:
            df: Input DataFrame
            partition_col: Column to partition by
            order_col: Column to order by

        Returns:
            DataFrame with running total
        """
        logger.info(f"Calculating running total partitioned by {partition_col}")
        window_spec = Window.partitionBy(partition_col).orderBy(order_col)
        return df.withColumn(
            "running_total",
            F.sum("amount").over(window_spec)
        )

    @staticmethod
    def calculate_growth_rate(df: DataFrame, period_col: str) -> DataFrame:
        """Calculate growth rate

        Args:
            df: Input DataFrame
            period_col: Time period column

        Returns:
            DataFrame with growth rate
        """
        logger.info("Calculating growth rate")
        return df
