"""
Configuration management for test automation framework
Loads environment variables and provides centralized configuration access
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    """Central configuration class for test framework"""

    # Environment
    ENV = os.getenv('ENV', 'dev')

    # Application URLs
    BASE_URL = os.getenv('BASE_URL', 'https://example.com')
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://api.example.com')

    # Browser Configuration
    BROWSER = os.getenv('BROWSER', 'chrome').lower()
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'

    # Timeout Configuration (in seconds)
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))
    EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', '20'))
    PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', '30'))

    # Test Data
    TEST_USER_EMAIL = os.getenv('TEST_USER_EMAIL', 'test@example.com')
    TEST_USER_PASSWORD = os.getenv('TEST_USER_PASSWORD', 'TestPassword123')

    # Project Paths
    PROJECT_ROOT = Path(__file__).parent.parent
    REPORTS_DIR = PROJECT_ROOT / 'reports'
    LOGS_DIR = PROJECT_ROOT / 'logs'
    DATA_DIR = PROJECT_ROOT / 'data'
    DRIVERS_DIR = PROJECT_ROOT / 'drivers'
    SCREENSHOTS_DIR = REPORTS_DIR / 'screenshots'

    # Reporting
    GENERATE_ALLURE_REPORT = os.getenv('GENERATE_ALLURE_REPORT', 'true').lower() == 'true'
    SCREENSHOT_ON_FAILURE = os.getenv('SCREENSHOT_ON_FAILURE', 'true').lower() == 'true'

    # Parallel Execution
    PARALLEL_WORKERS = int(os.getenv('PARALLEL_WORKERS', '4'))

    # Database Configuration (if needed)
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'test_db')
    DB_USER = os.getenv('DB_USER', 'test_user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'test_password')

    @classmethod
    def create_directories(cls):
        """Create necessary directories if they don't exist"""
        for directory in [cls.REPORTS_DIR, cls.LOGS_DIR, cls.SCREENSHOTS_DIR]:
            directory.mkdir(parents=True, exist_ok=True)

    @classmethod
    def get_config_summary(cls):
        """Get a summary of current configuration"""
        return {
            'environment': cls.ENV,
            'base_url': cls.BASE_URL,
            'browser': cls.BROWSER,
            'headless': cls.HEADLESS,
            'implicit_wait': cls.IMPLICIT_WAIT,
            'parallel_workers': cls.PARALLEL_WORKERS
        }


# Create directories on import
Config.create_directories()
