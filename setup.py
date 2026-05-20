"""Setup configuration for Sales Analytics Engine"""

from setuptools import setup, find_packages

setup(
    name="sales-analytics-engine",
    version="0.1.0",
    description="PySpark-based sales analytics engine",
    author="Data Analytics Team",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pyspark>=3.4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
        ]
    },
)
