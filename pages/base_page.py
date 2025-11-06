"""
Base Page Object Model class
Provides common functionality for all page objects
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.config import Config
import logging

logger = logging.getLogger(__name__)


class BasePage:
    """Base page class with common page object methods"""

    def __init__(self, driver):
        """
        Initialize base page

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.actions = ActionChains(driver)

    def navigate_to(self, url):
        """
        Navigate to a specific URL

        Args:
            url: URL to navigate to
        """
        logger.info(f"Navigating to: {url}")
        self.driver.get(url)

    def get_current_url(self):
        """Get current page URL"""
        return self.driver.current_url

    def get_page_title(self):
        """Get current page title"""
        return self.driver.title

    def wait_for_element(self, locator, timeout=None):
        """
        Wait for element to be visible

        Args:
            locator: Tuple of (By, locator_string)
            timeout: Custom timeout (optional)

        Returns:
            WebElement: Found element
        """
        try:
            wait = WebDriverWait(self.driver, timeout or Config.EXPLICIT_WAIT)
            element = wait.until(EC.visibility_of_element_located(locator))
            logger.debug(f"Element found: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Timeout waiting for element: {locator}")
            raise

    def wait_for_element_clickable(self, locator, timeout=None):
        """
        Wait for element to be clickable

        Args:
            locator: Tuple of (By, locator_string)
            timeout: Custom timeout (optional)

        Returns:
            WebElement: Clickable element
        """
        try:
            wait = WebDriverWait(self.driver, timeout or Config.EXPLICIT_WAIT)
            element = wait.until(EC.element_to_be_clickable(locator))
            return element
        except TimeoutException:
            logger.error(f"Timeout waiting for clickable element: {locator}")
            raise

    def find_element(self, locator):
        """
        Find element by locator

        Args:
            locator: Tuple of (By, locator_string)

        Returns:
            WebElement: Found element
        """
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            logger.error(f"Element not found: {locator}")
            raise

    def find_elements(self, locator):
        """
        Find multiple elements by locator

        Args:
            locator: Tuple of (By, locator_string)

        Returns:
            list: List of WebElements
        """
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """
        Click on element

        Args:
            locator: Tuple of (By, locator_string)
        """
        element = self.wait_for_element_clickable(locator)
        logger.info(f"Clicking element: {locator}")
        element.click()

    def enter_text(self, locator, text):
        """
        Enter text into input field

        Args:
            locator: Tuple of (By, locator_string)
            text: Text to enter
        """
        element = self.wait_for_element(locator)
        element.clear()
        logger.info(f"Entering text into {locator}: {text}")
        element.send_keys(text)

    def get_text(self, locator):
        """
        Get text from element

        Args:
            locator: Tuple of (By, locator_string)

        Returns:
            str: Element text
        """
        element = self.wait_for_element(locator)
        return element.text

    def get_attribute(self, locator, attribute):
        """
        Get attribute value from element

        Args:
            locator: Tuple of (By, locator_string)
            attribute: Attribute name

        Returns:
            str: Attribute value
        """
        element = self.wait_for_element(locator)
        return element.get_attribute(attribute)

    def is_element_visible(self, locator, timeout=5):
        """
        Check if element is visible

        Args:
            locator: Tuple of (By, locator_string)
            timeout: Time to wait (seconds)

        Returns:
            bool: True if visible, False otherwise
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_present(self, locator):
        """
        Check if element is present in DOM

        Args:
            locator: Tuple of (By, locator_string)

        Returns:
            bool: True if present, False otherwise
        """
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def scroll_to_element(self, locator):
        """
        Scroll to element

        Args:
            locator: Tuple of (By, locator_string)
        """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        logger.debug(f"Scrolled to element: {locator}")

    def hover_over_element(self, locator):
        """
        Hover over element

        Args:
            locator: Tuple of (By, locator_string)
        """
        element = self.wait_for_element(locator)
        self.actions.move_to_element(element).perform()
        logger.debug(f"Hovered over element: {locator}")

    def switch_to_frame(self, locator):
        """
        Switch to iframe

        Args:
            locator: Tuple of (By, locator_string) or frame index
        """
        if isinstance(locator, int):
            self.driver.switch_to.frame(locator)
        else:
            frame = self.wait_for_element(locator)
            self.driver.switch_to.frame(frame)
        logger.debug(f"Switched to frame: {locator}")

    def switch_to_default_content(self):
        """Switch back to default content"""
        self.driver.switch_to.default_content()
        logger.debug("Switched to default content")

    def accept_alert(self):
        """Accept JavaScript alert"""
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert.accept()
            logger.info("Alert accepted")
        except TimeoutException:
            logger.warning("No alert present to accept")

    def dismiss_alert(self):
        """Dismiss JavaScript alert"""
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert.dismiss()
            logger.info("Alert dismissed")
        except TimeoutException:
            logger.warning("No alert present to dismiss")

    def get_alert_text(self):
        """
        Get alert text

        Returns:
            str: Alert message text
        """
        try:
            alert = self.wait.until(EC.alert_is_present())
            return alert.text
        except TimeoutException:
            logger.warning("No alert present")
            return None

    def execute_script(self, script, *args):
        """
        Execute JavaScript

        Args:
            script: JavaScript code to execute
            *args: Arguments to pass to script

        Returns:
            Any: Script execution result
        """
        return self.driver.execute_script(script, *args)

    def refresh_page(self):
        """Refresh current page"""
        logger.info("Refreshing page")
        self.driver.refresh()

    def go_back(self):
        """Navigate back in browser history"""
        logger.info("Navigating back")
        self.driver.back()

    def go_forward(self):
        """Navigate forward in browser history"""
        logger.info("Navigating forward")
        self.driver.forward()

    def take_screenshot(self, filename):
        """
        Take screenshot

        Args:
            filename: Screenshot filename
        """
        filepath = Config.SCREENSHOTS_DIR / filename
        self.driver.save_screenshot(str(filepath))
        logger.info(f"Screenshot saved: {filepath}")
        return filepath
