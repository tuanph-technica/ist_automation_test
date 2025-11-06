"""
Sample Login Page Object
Demonstrates page object pattern implementation
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    """Login page object with locators and methods"""

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot Password?")
    REMEMBER_ME_CHECKBOX = (By.ID, "remember-me")

    def __init__(self, driver):
        """Initialize login page"""
        super().__init__(driver)
        self.page_url = f"{self.driver.current_url}/login"

    def navigate_to_login(self):
        """Navigate to login page"""
        self.navigate_to(self.page_url)
        logger.info("Navigated to login page")

    def enter_username(self, username):
        """
        Enter username

        Args:
            username: Username to enter
        """
        self.enter_text(self.USERNAME_INPUT, username)
        logger.info(f"Entered username: {username}")

    def enter_password(self, password):
        """
        Enter password

        Args:
            password: Password to enter
        """
        self.enter_text(self.PASSWORD_INPUT, password)
        logger.info("Entered password")

    def click_login_button(self):
        """Click login button"""
        self.click(self.LOGIN_BUTTON)
        logger.info("Clicked login button")

    def login(self, username, password):
        """
        Perform login action

        Args:
            username: Username
            password: Password
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        logger.info(f"Performed login with username: {username}")

    def get_error_message(self):
        """
        Get error message text

        Returns:
            str: Error message
        """
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_message_displayed(self):
        """
        Check if error message is displayed

        Returns:
            bool: True if displayed
        """
        return self.is_element_visible(self.ERROR_MESSAGE)

    def click_forgot_password(self):
        """Click forgot password link"""
        self.click(self.FORGOT_PASSWORD_LINK)
        logger.info("Clicked forgot password link")

    def toggle_remember_me(self):
        """Toggle remember me checkbox"""
        self.click(self.REMEMBER_ME_CHECKBOX)
        logger.info("Toggled remember me checkbox")

    def is_remember_me_selected(self):
        """
        Check if remember me is selected

        Returns:
            bool: True if selected
        """
        element = self.find_element(self.REMEMBER_ME_CHECKBOX)
        return element.is_selected()
