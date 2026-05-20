"""Sales data processor for analytics"""

from pyspark.sql import SparkSession, DataFrame

from src.logger import setup_logger

logger = setup_logger(__name__)


class SalesProcessor:
    """Process sales data and prepare it for analysis"""

    def __init__(self, spark: SparkSession, config):
        """Initialize the sales processor

        Args:
            spark: SparkSession instance
            config: Configuration object
        """
        self.spark = spark
        self.config = config
        logger.info("SalesProcessor initialized")

    def load_sales_data(self, path: str) -> DataFrame:
        """Load sales data from a given path

        Args:
            path: Path to sales data

        Returns:
            DataFrame containing sales data
        """
        logger.info(f"Loading sales data from {path}")
        return self.spark.read.option("header", "true").option(
            "inferSchema", "true"
        ).csv(path)

    def process(self, data: DataFrame) -> DataFrame:
        """Process sales data

        Args:
            data: Input DataFrame

        Returns:
            Processed DataFrame
        """
        logger.info("Processing sales data")
        return data
