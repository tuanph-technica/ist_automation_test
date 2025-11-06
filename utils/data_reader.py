"""
Data reader utility for test data management
Supports JSON, YAML, CSV, and Excel formats
"""
import json
import yaml
import csv
import pandas as pd
from pathlib import Path
from config.config import Config
import logging

logger = logging.getLogger(__name__)


class DataReader:
    """Utility class for reading test data from various sources"""

    @staticmethod
    def read_json(filename):
        """
        Read JSON file

        Args:
            filename: JSON filename in data directory

        Returns:
            dict: Parsed JSON data
        """
        filepath = Config.DATA_DIR / filename
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                logger.info(f"Successfully read JSON file: {filepath}")
                return data
        except FileNotFoundError:
            logger.error(f"JSON file not found: {filepath}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing JSON file: {e}")
            raise

    @staticmethod
    def read_yaml(filename):
        """
        Read YAML file

        Args:
            filename: YAML filename in data directory

        Returns:
            dict: Parsed YAML data
        """
        filepath = Config.DATA_DIR / filename
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                logger.info(f"Successfully read YAML file: {filepath}")
                return data
        except FileNotFoundError:
            logger.error(f"YAML file not found: {filepath}")
            raise
        except yaml.YAMLError as e:
            logger.error(f"Error parsing YAML file: {e}")
            raise

    @staticmethod
    def read_csv(filename):
        """
        Read CSV file

        Args:
            filename: CSV filename in data directory

        Returns:
            list: List of dictionaries (each row as dict)
        """
        filepath = Config.DATA_DIR / filename
        try:
            data = []
            with open(filepath, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)
                logger.info(f"Successfully read CSV file: {filepath}")
                return data
        except FileNotFoundError:
            logger.error(f"CSV file not found: {filepath}")
            raise

    @staticmethod
    def read_excel(filename, sheet_name=0):
        """
        Read Excel file

        Args:
            filename: Excel filename in data directory
            sheet_name: Sheet name or index (default: 0)

        Returns:
            list: List of dictionaries (each row as dict)
        """
        filepath = Config.DATA_DIR / filename
        try:
            df = pd.read_excel(filepath, sheet_name=sheet_name)
            data = df.to_dict('records')
            logger.info(f"Successfully read Excel file: {filepath}, sheet: {sheet_name}")
            return data
        except FileNotFoundError:
            logger.error(f"Excel file not found: {filepath}")
            raise
        except Exception as e:
            logger.error(f"Error reading Excel file: {e}")
            raise

    @staticmethod
    def write_json(data, filename):
        """
        Write data to JSON file

        Args:
            data: Data to write
            filename: Output filename
        """
        filepath = Config.DATA_DIR / filename
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                logger.info(f"Successfully wrote JSON file: {filepath}")
        except Exception as e:
            logger.error(f"Error writing JSON file: {e}")
            raise
