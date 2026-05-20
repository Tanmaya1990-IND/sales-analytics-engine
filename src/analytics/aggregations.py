"""Aggregation functions for sales analytics"""

from pyspark.sql import DataFrame
from pyspark.sql import functions as F

from src.logger import setup_logger

logger = setup_logger(__name__)


class Aggregations:
    """Perform aggregations on sales data"""

    @staticmethod
    def by_region(df: DataFrame) -> DataFrame:
        """Aggregate sales by region

        Args:
            df: Input DataFrame

        Returns:
            Aggregated DataFrame
        """
        logger.info("Aggregating sales by region")
        return df.groupBy("region").agg(F.sum("amount").alias("total_sales"))

    @staticmethod
    def by_product(df: DataFrame) -> DataFrame:
        """Aggregate sales by product

        Args:
            df: Input DataFrame

        Returns:
            Aggregated DataFrame
        """
        logger.info("Aggregating sales by product")
        return df.groupBy("product").agg(F.sum("amount").alias("total_sales"))

    @staticmethod
    def by_date(df: DataFrame) -> DataFrame:
        """Aggregate sales by date

        Args:
            df: Input DataFrame

        Returns:
            Aggregated DataFrame
        """
        logger.info("Aggregating sales by date")
        return df.groupBy("date").agg(F.sum("amount").alias("daily_sales"))
