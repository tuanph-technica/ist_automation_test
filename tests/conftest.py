"""
Pytest configuration and fixtures
Shared fixtures available to all test modules
"""
import pytest
from selenium import webdriver
from config.browser_config import BrowserConfig
from config.config import Config
from utils.screenshot_helper import ScreenshotHelper
from utils.logger import get_logger
import logging

logger = get_logger(__name__)


@pytest.fixture(scope="function")
def driver(request):
    """
    WebDriver fixture with automatic cleanup
    Scope: function (new driver for each test)

    Usage:
        def test_example(driver):
            driver.get("https://example.com")
    """
    logger.info(f"Initializing WebDriver: {Config.BROWSER}")
    driver_instance = BrowserConfig.create_driver()

    yield driver_instance

    # Cleanup
    logger.info("Closing WebDriver")
    driver_instance.quit()


@pytest.fixture(scope="session")
def session_driver():
    """
    Session-scoped WebDriver fixture
    Reuses same driver instance across test session

    Usage:
        def test_example(session_driver):
            session_driver.get("https://example.com")
    """
    logger.info(f"Initializing session WebDriver: {Config.BROWSER}")
    driver_instance = BrowserConfig.create_driver()

    yield driver_instance

    logger.info("Closing session WebDriver")
    driver_instance.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results and take screenshots on failure
    """
    outcome = yield
    report = outcome.get_result()

    # Take screenshot on test failure
    if report.when == "call" and report.failed:
        if Config.SCREENSHOT_ON_FAILURE:
            driver = None
            # Try to get driver from test fixtures
            if "driver" in item.funcargs:
                driver = item.funcargs["driver"]
            elif "session_driver" in item.funcargs:
                driver = item.funcargs["session_driver"]

            if driver:
                test_name = item.nodeid.replace("::", "_").replace("/", "_")
                ScreenshotHelper.take_screenshot_on_failure(driver, test_name)
                logger.info(f"Screenshot captured for failed test: {test_name}")


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """
    Session setup and teardown
    Runs once at the beginning and end of test session
    """
    logger.info("=" * 80)
    logger.info("TEST SESSION STARTED")
    logger.info(f"Configuration: {Config.get_config_summary()}")
    logger.info("=" * 80)

    # Setup code here
    Config.create_directories()

    yield

    # Teardown code here
    logger.info("=" * 80)
    logger.info("TEST SESSION COMPLETED")
    logger.info("=" * 80)


@pytest.fixture
def test_data():
    """
    Fixture to provide test data
    Can be customized to read from files

    Returns:
        dict: Test data dictionary
    """
    return {
        "valid_username": Config.TEST_USER_EMAIL,
        "valid_password": Config.TEST_USER_PASSWORD,
        "invalid_username": "invalid@example.com",
        "invalid_password": "wrongpassword"
    }


@pytest.fixture
def base_url():
    """
    Fixture to provide base URL

    Returns:
        str: Application base URL
    """
    return Config.BASE_URL


# Pytest command line options
def pytest_addoption(parser):
    """Add custom command line options"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome, firefox, edge"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests: dev, staging, prod"
    )


@pytest.fixture(scope="session")
def browser_option(request):
    """Get browser option from command line"""
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def headless_option(request):
    """Get headless option from command line"""
    return request.config.getoption("--headless")


@pytest.fixture(scope="session")
def env_option(request):
    """Get environment option from command line"""
    return request.config.getoption("--env")
