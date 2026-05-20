"""Main entry point for the sales analytics engine"""

import os
import csv
from pyspark.sql import SparkSession

from src.config import get_config
from src.logger import setup_logger
from src.analytics import SalesProcessor

logger = setup_logger(__name__)


def create_sample_csv() -> str:
    """Create sample sales data as CSV file"""
    logger.info("Creating sample sales data")

    # Create data directory
    os.makedirs("./data/raw", exist_ok=True)
    csv_path = "./data/raw/sales_sample.csv"

    # Sample data
    sales_data = [
        ("date", "product", "region", "amount"),
        ("2024-01-01", "Product A", "North", "1000.0"),
        ("2024-01-01", "Product B", "South", "1500.0"),
        ("2024-01-01", "Product A", "East", "800.0"),
        ("2024-01-02", "Product C", "West", "2000.0"),
        ("2024-01-02", "Product A", "North", "1200.0"),
        ("2024-01-02", "Product B", "South", "1800.0"),
        ("2024-01-03", "Product B", "East", "950.0"),
        ("2024-01-03", "Product C", "North", "2200.0"),
        ("2024-01-03", "Product A", "West", "1100.0"),
    ]

    # Write CSV file
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sales_data)

    logger.info(f"Sample data saved to {csv_path}")
    return csv_path


def main():
    """Main function to run the sales analytics engine"""
    config = get_config()
    logger.info(f"Starting Sales Analytics Engine (DEBUG: {config.DEBUG})")
    logger.info(f"Environment: {'development' if config.DEBUG else 'production'}")

    spark = SparkSession.builder.appName(
        config.SPARK_APP_NAME
    ).master(config.SPARK_MASTER).config(
        "spark.sql.shuffle.partitions", "1"
    ).getOrCreate()

    # Suppress Spark warnings
    spark.sparkContext.setLogLevel("ERROR")

    try:
        processor = SalesProcessor(spark, config)
        logger.info("Sales processor initialized successfully")

        # Create sample CSV file
        csv_path = create_sample_csv()

        # Load sample data
        logger.info("Loading sales data")
        sales_df = processor.load_sales_data(csv_path)

        record_count = sales_df.count()
        logger.info(f"Loaded {record_count} records")

        logger.info("Data Schema:")
        sales_df.printSchema()

        # Process data
        logger.info("\nProcessing data")
        processed_df = processor.process(sales_df)

        # Show sample results
        logger.info("\nSample data (first 5 rows):")
        processed_df.show(5, truncate=False)

        # Display statistics
        logger.info(f"\nTotal records processed: {processed_df.count()}")

        # Save results locally with Python (avoid Hadoop issues on Windows)
        logger.info("\nSaving results")
        os.makedirs(config.OUTPUT_PATH, exist_ok=True)

        try:
            output_csv = f"{config.OUTPUT_PATH}/processed_sales.csv"
            records = processed_df.collect()
            with open(output_csv, 'w', newline='') as f:
                writer = csv.writer(f)
                # Write header
                writer.writerow(processed_df.columns)
                # Write data
                for row in records:
                    writer.writerow(row)
            logger.info(f"Results saved to {output_csv}")
        except Exception as e:
            logger.warning(f"Could not save results: {e}")

        logger.info("\n" + "="*50)
        logger.info("EXECUTION SUMMARY")
        logger.info("="*50)
        logger.info(f"Input file: {csv_path}")
        logger.info(f"Output directory: {config.OUTPUT_PATH}")
        logger.info(f"Records processed: {processed_df.count()}")
        logger.info("Status: Completed successfully [OK]")
        logger.info("="*50)

    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        raise
    finally:
        spark.stop()
        logger.info("Spark session stopped")


if __name__ == "__main__":
    main()
