"""
Screenshot utility for capturing test evidence
"""
from datetime import datetime
from pathlib import Path
from config.config import Config
import logging

logger = logging.getLogger(__name__)


class ScreenshotHelper:
    """Helper class for managing screenshots"""

    @staticmethod
    def take_screenshot(driver, test_name, description=""):
        """
        Take screenshot with timestamp

        Args:
            driver: WebDriver instance
            test_name: Test case name
            description: Additional description

        Returns:
            Path: Screenshot file path
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{test_name}_{description}_{timestamp}.png" if description else f"{test_name}_{timestamp}.png"
        filepath = Config.SCREENSHOTS_DIR / filename

        try:
            driver.save_screenshot(str(filepath))
            logger.info(f"Screenshot saved: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
            return None

    @staticmethod
    def take_screenshot_on_failure(driver, test_name):
        """
        Take screenshot for failed test

        Args:
            driver: WebDriver instance
            test_name: Test case name

        Returns:
            Path: Screenshot file path
        """
        return ScreenshotHelper.take_screenshot(driver, test_name, "FAILURE")

    @staticmethod
    def cleanup_old_screenshots(days=7):
        """
        Clean up screenshots older than specified days

        Args:
            days: Number of days to keep screenshots
        """
        try:
            current_time = datetime.now()
            for screenshot in Config.SCREENSHOTS_DIR.glob("*.png"):
                file_time = datetime.fromtimestamp(screenshot.stat().st_mtime)
                if (current_time - file_time).days > days:
                    screenshot.unlink()
                    logger.info(f"Deleted old screenshot: {screenshot}")
        except Exception as e:
            logger.error(f"Error cleaning up screenshots: {e}")
