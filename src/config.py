"""Configuration management for the sales analytics engine"""

import os
from typing import Optional


class Config:
    """Base configuration class"""

    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    SPARK_APP_NAME: str = os.getenv("SPARK_APP_NAME", "SalesAnalyticsEngine")
    DATA_PATH: str = os.getenv("DATA_PATH", "./data")
    OUTPUT_PATH: str = os.getenv("OUTPUT_PATH", "./data/outputs")


class DevelopmentConfig(Config):
    """Development configuration"""

    DEBUG: bool = True
    SPARK_MASTER: str = "local[*]"


class ProductionConfig(Config):
    """Production configuration"""

    DEBUG: bool = False
    SPARK_MASTER: str = os.getenv("SPARK_MASTER", "yarn")


def get_config(env: Optional[str] = None) -> Config:
    """Get configuration based on environment"""
    environment = env or os.getenv("ENV", "development")

    if environment == "production":
        return ProductionConfig()
    return DevelopmentConfig()
