# IST Automation Test Framework

A comprehensive Selenium Python automation testing framework for web applications with Page Object Model (POM) architecture.

## 🎯 Features

- **Page Object Model (POM)**: Clean separation of test logic and page interactions
- **Multi-Browser Support**: Chrome, Firefox, Edge with easy configuration
- **Flexible Configuration**: Environment-based configuration with `.env` support
- **Advanced Reporting**: HTML reports, Allure integration, screenshot capture
- **Parallel Execution**: Run tests in parallel for faster execution
- **Logging**: Colored console logs and detailed file logging
- **Test Data Management**: Support for JSON, YAML, CSV, Excel
- **Custom Wait Utilities**: Enhanced wait conditions and helpers
- **Pytest Integration**: Markers, fixtures, parametrization support

## 📁 Project Structure

```
ist_automation_test/
├── config/                    # Configuration files
│   ├── __init__.py
│   ├── config.py             # Central configuration management
│   └── browser_config.py     # Browser setup and WebDriver config
├── pages/                     # Page Object Models
│   ├── __init__.py
│   ├── base_page.py          # Base page with common methods
│   └── sample_login_page.py  # Example login page object
├── tests/                     # Test files
│   ├── __init__.py
│   ├── conftest.py           # Pytest fixtures and hooks
│   ├── test_cases/           # Test case modules
│   │   ├── __init__.py
│   │   └── test_sample_login.py
│   └── test_suites/          # Test suite configurations
├── utils/                     # Utility modules
│   ├── __init__.py
│   ├── logger.py             # Logging utilities
│   ├── screenshot_helper.py  # Screenshot management
│   ├── data_reader.py        # Test data readers
│   └── wait_helper.py        # Custom wait helpers
├── data/                      # Test data files
│   └── sample_test_data.json
├── reports/                   # Test reports (auto-generated)
├── logs/                      # Log files (auto-generated)
├── drivers/                   # WebDriver binaries (optional)
├── requirements.txt           # Python dependencies
├── pytest.ini                 # Pytest configuration
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Chrome/Firefox/Edge browser installed

### Installation

1. **Clone the repository**
   ```bash
   cd ist_automation_test
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

## ⚙️ Configuration

### Environment Variables (.env)

```env
# Environment
ENV=dev

# Application URLs
BASE_URL=https://your-app-url.com
API_BASE_URL=https://api.your-app-url.com

# Browser Configuration
BROWSER=chrome              # chrome, firefox, edge
HEADLESS=false             # true for headless mode
IMPLICIT_WAIT=10
EXPLICIT_WAIT=20
PAGE_LOAD_TIMEOUT=30

# Test Data
TEST_USER_EMAIL=test@example.com
TEST_USER_PASSWORD=TestPassword123

# Reporting
GENERATE_ALLURE_REPORT=true
SCREENSHOT_ON_FAILURE=true

# Parallel Execution
PARALLEL_WORKERS=4
```

## 🧪 Running Tests

### Basic Test Execution

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_cases/test_sample_login.py

# Run specific test
pytest tests/test_cases/test_sample_login.py::TestLogin::test_valid_login

# Run with verbose output
pytest -v

# Run tests in parallel
pytest -n auto
```

### Run by Markers

```bash
# Run smoke tests
pytest -m smoke

# Run regression tests
pytest -m regression

# Run critical tests
pytest -m critical

# Run UI tests only
pytest -m ui

# Exclude slow tests
pytest -m "not slow"
```

### Browser Selection

```bash
# Run with Chrome (default)
pytest --browser=chrome

# Run with Firefox
pytest --browser=firefox

# Run with Edge
pytest --browser=edge

# Run in headless mode
pytest --headless
```

### Environment Selection

```bash
# Run in dev environment
pytest --env=dev

# Run in staging environment
pytest --env=staging

# Run in production environment
pytest --env=prod
```

### Generate Reports

```bash
# HTML report (generated automatically)
pytest --html=reports/report.html

# Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

## 📝 Writing Tests

### Basic Test Structure

```python
import pytest
from pages.sample_login_page import LoginPage
from utils.logger import get_logger

logger = get_logger(__name__)

class TestLogin:

    @pytest.mark.smoke
    def test_valid_login(self, driver, test_data):
        """Test successful login"""
        logger.info("Starting test: test_valid_login")

        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.login(
            test_data["valid_username"],
            test_data["valid_password"]
        )

        # Add assertions
        assert "Dashboard" in driver.title

        logger.info("Test completed successfully")
```

### Creating Page Objects

```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = f"{self.driver.current_url}/login"

    def login(self, username, password):
        """Perform login"""
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
```

### Using Test Data

```python
# From JSON file
from utils.data_reader import DataReader

test_data = DataReader.read_json("sample_test_data.json")
users = test_data["users"]

# From CSV file
csv_data = DataReader.read_csv("test_users.csv")

# From Excel file
excel_data = DataReader.read_excel("test_data.xlsx", sheet_name="Users")
```

## 📊 Test Markers

Available pytest markers defined in `pytest.ini`:

- `@pytest.mark.smoke` - Quick smoke tests
- `@pytest.mark.regression` - Full regression suite
- `@pytest.mark.sanity` - Sanity check tests
- `@pytest.mark.critical` - Critical path tests
- `@pytest.mark.slow` - Tests that take significant time
- `@pytest.mark.ui` - UI-related tests
- `@pytest.mark.api` - API integration tests

## 🔧 Utilities

### Logger

```python
from utils.logger import get_logger

logger = get_logger(__name__)
logger.info("Information message")
logger.warning("Warning message")
logger.error("Error message")
```

### Screenshot Helper

```python
from utils.screenshot_helper import ScreenshotHelper

# Take screenshot
ScreenshotHelper.take_screenshot(driver, "test_name", "description")

# Automatic on test failure (configured in conftest.py)
```

### Custom Wait Conditions

```python
from utils.wait_helper import WaitHelper

# Wait for URL
WaitHelper.wait_for_url_contains(driver, "/dashboard")

# Wait for specific element count
WaitHelper.wait_for_element_count(driver, locator, count=5)

# Wait for element text
WaitHelper.wait_for_element_text(driver, locator, "Expected Text")
```

## 📈 Reporting

### HTML Report

Automatically generated after test execution:
- Location: `reports/report.html`
- Includes test results, duration, screenshots

### Allure Report

Generate interactive Allure report:

```bash
# Run tests with Allure
pytest --alluredir=allure-results

# Generate and open report
allure serve allure-results
```

### Logs

- Console logs: Colored output with timestamps
- File logs: `logs/test_execution.log`

## 🎯 Best Practices

1. **Use Page Object Model**: Keep test logic separate from page interactions
2. **Use Markers**: Tag tests appropriately for selective execution
3. **Explicit Waits**: Use explicit waits instead of `time.sleep()`
4. **Logging**: Add meaningful log messages for debugging
5. **Screenshots**: Automatic screenshots on failure (enabled by default)
6. **Data-Driven**: Use external data files for test data
7. **DRY Principle**: Don't repeat yourself - use fixtures and utilities
8. **Assertions**: Use clear, descriptive assertion messages

## 🐛 Troubleshooting

### WebDriver Issues

```bash
# Update WebDriver
pip install --upgrade webdriver-manager

# Clear WebDriver cache
rm -rf ~/.wdm
```

### Permission Issues

```bash
# On Linux/Mac, make sure drivers are executable
chmod +x drivers/*
```

### Dependencies Issues

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 🤝 Contributing

1. Create feature branch
2. Add/update tests
3. Ensure all tests pass
4. Submit pull request

## 📄 License

This project is for internal testing purposes.

## 📞 Support

For issues or questions, please contact the QA team.

---

**Happy Testing! 🚀**
