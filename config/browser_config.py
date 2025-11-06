"""
Browser configuration and WebDriver setup
Supports Chrome, Firefox, Edge with various options
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from config.config import Config


class BrowserConfig:
    """Browser configuration and WebDriver initialization"""

    @staticmethod
    def get_chrome_options():
        """Configure Chrome browser options"""
        options = webdriver.ChromeOptions()

        if Config.HEADLESS:
            options.add_argument('--headless=new')

        # Standard options for stability
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-infobars')
        options.add_argument('--start-maximized')
        options.add_argument('--ignore-certificate-errors')

        # Performance options
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)

        # Preferences
        prefs = {
            'download.default_directory': str(Config.REPORTS_DIR),
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'safebrowsing.enabled': False
        }
        options.add_experimental_option('prefs', prefs)

        return options

    @staticmethod
    def get_firefox_options():
        """Configure Firefox browser options"""
        options = webdriver.FirefoxOptions()

        if Config.HEADLESS:
            options.add_argument('--headless')

        options.add_argument('--width=1920')
        options.add_argument('--height=1080')

        # Preferences
        options.set_preference('browser.download.folderList', 2)
        options.set_preference('browser.download.dir', str(Config.REPORTS_DIR))
        options.set_preference('browser.download.useDownloadDir', True)
        options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')

        return options

    @staticmethod
    def get_edge_options():
        """Configure Edge browser options"""
        options = webdriver.EdgeOptions()

        if Config.HEADLESS:
            options.add_argument('--headless=new')

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--start-maximized')

        return options

    @staticmethod
    def create_driver(browser_name=None):
        """
        Create and configure WebDriver instance

        Args:
            browser_name: Browser to use (chrome, firefox, edge). Defaults to Config.BROWSER

        Returns:
            WebDriver: Configured WebDriver instance
        """
        browser = (browser_name or Config.BROWSER).lower()

        driver = None

        if browser == 'chrome':
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=BrowserConfig.get_chrome_options())

        elif browser == 'firefox':
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=BrowserConfig.get_firefox_options())

        elif browser == 'edge':
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service, options=BrowserConfig.get_edge_options())

        else:
            raise ValueError(f"Unsupported browser: {browser}. Supported: chrome, firefox, edge")

        # Apply timeouts
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)

        return driver
