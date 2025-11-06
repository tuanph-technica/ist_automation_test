"""
Sample login test cases
Demonstrates test structure and best practices
"""
import pytest
from pages.sample_login_page import LoginPage
from config.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)


class TestLogin:
    """Login test suite"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_valid_login(self, driver, test_data):
        """
        Test successful login with valid credentials

        Steps:
            1. Navigate to login page
            2. Enter valid username
            3. Enter valid password
            4. Click login button
            5. Verify successful login

        Expected: User successfully logged in
        """
        logger.info("Starting test: test_valid_login")

        login_page = LoginPage(driver)
        login_page.navigate_to_login()

        # Perform login
        login_page.login(
            test_data["valid_username"],
            test_data["valid_password"]
        )

        # Assertions
        # Note: Add actual assertions based on your application
        # Example: assert "Dashboard" in driver.title
        logger.info("Test completed: test_valid_login")

    @pytest.mark.smoke
    def test_invalid_login(self, driver, test_data):
        """
        Test login with invalid credentials

        Steps:
            1. Navigate to login page
            2. Enter invalid username
            3. Enter invalid password
            4. Click login button
            5. Verify error message displayed

        Expected: Error message shown, login fails
        """
        logger.info("Starting test: test_invalid_login")

        login_page = LoginPage(driver)
        login_page.navigate_to_login()

        # Attempt login with invalid credentials
        login_page.login(
            test_data["invalid_username"],
            test_data["invalid_password"]
        )

        # Verify error message
        assert login_page.is_error_message_displayed(), "Error message not displayed"
        error_text = login_page.get_error_message()
        logger.info(f"Error message displayed: {error_text}")

        logger.info("Test completed: test_invalid_login")

    @pytest.mark.regression
    def test_empty_username(self, driver, test_data):
        """
        Test login with empty username field

        Steps:
            1. Navigate to login page
            2. Leave username empty
            3. Enter valid password
            4. Click login button
            5. Verify validation error

        Expected: Validation error for required username field
        """
        logger.info("Starting test: test_empty_username")

        login_page = LoginPage(driver)
        login_page.navigate_to_login()

        # Attempt login with empty username
        login_page.enter_password(test_data["valid_password"])
        login_page.click_login_button()

        # Verify error displayed
        assert login_page.is_error_message_displayed(), "Validation error not shown"

        logger.info("Test completed: test_empty_username")

    @pytest.mark.regression
    def test_empty_password(self, driver, test_data):
        """
        Test login with empty password field

        Steps:
            1. Navigate to login page
            2. Enter valid username
            3. Leave password empty
            4. Click login button
            5. Verify validation error

        Expected: Validation error for required password field
        """
        logger.info("Starting test: test_empty_password")

        login_page = LoginPage(driver)
        login_page.navigate_to_login()

        # Attempt login with empty password
        login_page.enter_username(test_data["valid_username"])
        login_page.click_login_button()

        # Verify error displayed
        assert login_page.is_error_message_displayed(), "Validation error not shown"

        logger.info("Test completed: test_empty_password")

    @pytest.mark.ui
    def test_remember_me_functionality(self, driver):
        """
        Test remember me checkbox functionality

        Steps:
            1. Navigate to login page
            2. Verify remember me checkbox visible
            3. Click checkbox
            4. Verify checkbox selected

        Expected: Remember me checkbox toggles correctly
        """
        logger.info("Starting test: test_remember_me_functionality")

        login_page = LoginPage(driver)
        login_page.navigate_to_login()

        # Test checkbox toggle
        initial_state = login_page.is_remember_me_selected()
        login_page.toggle_remember_me()
        new_state = login_page.is_remember_me_selected()

        assert initial_state != new_state, "Remember me checkbox did not toggle"

        logger.info("Test completed: test_remember_me_functionality")

    @pytest.mark.ui
    def test_forgot_password_link(self, driver):
        """
        Test forgot password link navigation

        Steps:
            1. Navigate to login page
            2. Click forgot password link
            3. Verify navigation to password recovery page

        Expected: User navigated to password recovery page
        """
        logger.info("Starting test: test_forgot_password_link")

        login_page = LoginPage(driver)
        login_page.navigate_to_login()

        # Click forgot password
        login_page.click_forgot_password()

        # Verify URL or page element
        # Example: assert "forgot-password" in driver.current_url

        logger.info("Test completed: test_forgot_password_link")


# Parametrized test example
@pytest.mark.parametrize("username,password,expected_result", [
    ("valid@example.com", "ValidPass123", "success"),
    ("invalid@example.com", "WrongPass", "failure"),
    ("", "ValidPass123", "failure"),
    ("valid@example.com", "", "failure"),
])
@pytest.mark.regression
def test_login_variations(driver, username, password, expected_result):
    """
    Parametrized test for multiple login scenarios

    Args:
        username: Username to test
        password: Password to test
        expected_result: Expected outcome (success/failure)
    """
    logger.info(f"Testing login with: {username} / {password}")

    login_page = LoginPage(driver)
    login_page.navigate_to_login()
    login_page.login(username, password)

    if expected_result == "failure":
        assert login_page.is_error_message_displayed(), \
            f"Expected error for {username}/{password}"

    logger.info(f"Login test completed: {expected_result}")
