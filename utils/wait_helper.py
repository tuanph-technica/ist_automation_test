"""
Custom wait helper utilities
Provides specialized wait conditions beyond Selenium defaults
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import Config
import logging

logger = logging.getLogger(__name__)


class WaitHelper:
    """Custom wait helper methods"""

    @staticmethod
    def wait_for_url_contains(driver, url_fragment, timeout=None):
        """
        Wait until URL contains specific fragment

        Args:
            driver: WebDriver instance
            url_fragment: URL fragment to wait for
            timeout: Custom timeout (optional)

        Returns:
            bool: True if successful
        """
        wait_time = timeout or Config.EXPLICIT_WAIT
        try:
            WebDriverWait(driver, wait_time).until(
                EC.url_contains(url_fragment)
            )
            logger.info(f"URL contains: {url_fragment}")
            return True
        except TimeoutException:
            logger.error(f"Timeout waiting for URL to contain: {url_fragment}")
            return False

    @staticmethod
    def wait_for_title_contains(driver, title_fragment, timeout=None):
        """
        Wait until page title contains specific text

        Args:
            driver: WebDriver instance
            title_fragment: Title fragment to wait for
            timeout: Custom timeout (optional)

        Returns:
            bool: True if successful
        """
        wait_time = timeout or Config.EXPLICIT_WAIT
        try:
            WebDriverWait(driver, wait_time).until(
                EC.title_contains(title_fragment)
            )
            logger.info(f"Title contains: {title_fragment}")
            return True
        except TimeoutException:
            logger.error(f"Timeout waiting for title to contain: {title_fragment}")
            return False

    @staticmethod
    def wait_for_element_count(driver, locator, count, timeout=None):
        """
        Wait until specific number of elements are present

        Args:
            driver: WebDriver instance
            locator: Element locator tuple
            count: Expected element count
            timeout: Custom timeout (optional)

        Returns:
            bool: True if successful
        """
        wait_time = timeout or Config.EXPLICIT_WAIT
        try:
            WebDriverWait(driver, wait_time).until(
                lambda d: len(d.find_elements(*locator)) == count
            )
            logger.info(f"Found {count} elements matching: {locator}")
            return True
        except TimeoutException:
            logger.error(f"Timeout waiting for {count} elements: {locator}")
            return False

    @staticmethod
    def wait_for_element_text(driver, locator, expected_text, timeout=None):
        """
        Wait until element text matches expected value

        Args:
            driver: WebDriver instance
            locator: Element locator tuple
            expected_text: Expected text value
            timeout: Custom timeout (optional)

        Returns:
            bool: True if successful
        """
        wait_time = timeout or Config.EXPLICIT_WAIT
        try:
            WebDriverWait(driver, wait_time).until(
                EC.text_to_be_present_in_element(locator, expected_text)
            )
            logger.info(f"Element text matches: {expected_text}")
            return True
        except TimeoutException:
            logger.error(f"Timeout waiting for element text: {expected_text}")
            return False

    @staticmethod
    def wait_for_element_invisible(driver, locator, timeout=None):
        """
        Wait until element becomes invisible

        Args:
            driver: WebDriver instance
            locator: Element locator tuple
            timeout: Custom timeout (optional)

        Returns:
            bool: True if successful
        """
        wait_time = timeout or Config.EXPLICIT_WAIT
        try:
            WebDriverWait(driver, wait_time).until(
                EC.invisibility_of_element_located(locator)
            )
            logger.info(f"Element became invisible: {locator}")
            return True
        except TimeoutException:
            logger.error(f"Timeout waiting for element to be invisible: {locator}")
            return False
