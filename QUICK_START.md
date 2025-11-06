# Quick Start Guide

Get started with the IST Automation Test Framework in 5 minutes.

## 🚀 Quick Setup

### 1. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings
# Update BASE_URL, TEST_USER_EMAIL, TEST_USER_PASSWORD
```

### 4. Run Sample Test

```bash
# Run a quick test to verify setup
pytest tests/test_cases/test_sample_login.py::TestLogin::test_remember_me_functionality -v
```

## 📝 Your First Test

### Create a Page Object

Create `pages/home_page.py`:

```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators
    LOGO = (By.CSS_SELECTOR, ".logo")
    SEARCH_BOX = (By.ID, "search")

    def search(self, query):
        self.enter_text(self.SEARCH_BOX, query)
        self.find_element(self.SEARCH_BOX).submit()
```

### Create a Test

Create `tests/test_cases/test_home.py`:

```python
import pytest
from pages.home_page import HomePage
from utils.logger import get_logger

logger = get_logger(__name__)

class TestHome:

    @pytest.mark.smoke
    def test_search_functionality(self, driver, base_url):
        logger.info("Testing search functionality")

        # Navigate to home page
        driver.get(base_url)

        # Use page object
        home_page = HomePage(driver)
        home_page.search("test query")

        # Assert
        assert "search" in driver.current_url
        logger.info("Search test passed")
```

### Run Your Test

```bash
pytest tests/test_cases/test_home.py -v
```

## 🎯 Common Commands

```bash
# Run all tests
pytest

# Run with markers
pytest -m smoke

# Run in parallel
pytest -n auto

# Generate HTML report
pytest --html=reports/report.html

# Run specific test
pytest tests/test_cases/test_home.py::TestHome::test_search_functionality

# Run in different browser
pytest --browser=firefox

# Run in headless mode
pytest --headless
```

## 📚 Project Structure Quick Reference

```
ist_automation_test/
├── config/              # Configuration files
├── pages/               # Page Object Models (add your pages here)
├── tests/               # Test files (add your tests here)
│   ├── conftest.py     # Pytest fixtures
│   └── test_cases/     # Test case modules
├── utils/               # Utility functions
├── data/                # Test data files
├── .env                 # Environment configuration
└── requirements.txt     # Python dependencies
```

## 🔍 Where to Add Your Code

1. **Page Objects**: Add to `pages/` directory
2. **Test Cases**: Add to `tests/test_cases/` directory
3. **Test Data**: Add to `data/` directory
4. **Utilities**: Add to `utils/` directory

## 💡 Tips

- Use `@pytest.mark.smoke` for critical tests
- Use `logger.info()` for debugging
- Screenshots are automatically taken on test failures
- Check `logs/test_execution.log` for detailed logs

## 🐛 Common Issues

**Issue**: Module not found
```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

**Issue**: WebDriver not found
```bash
# Let it auto-download on first run
pytest tests/test_cases/test_sample_login.py -k test_remember_me_functionality
```

**Issue**: Tests not found
```bash
# Ensure you're in project root
pwd
# Should show: .../ist_automation_test
```

## 📖 Next Steps

1. ✅ Read full [README.md](README.md) for detailed documentation
2. ✅ Check [SETUP_GUIDE.md](SETUP_GUIDE.md) for complete setup instructions
3. ✅ Customize page objects for your application
4. ✅ Write test cases for your features
5. ✅ Configure CI/CD pipeline

## 🎓 Learning Resources

- **Selenium Documentation**: https://selenium-python.readthedocs.io/
- **Pytest Documentation**: https://docs.pytest.org/
- **Page Object Pattern**: https://selenium-python.readthedocs.io/page-objects.html

---

**Ready to automate! 🚀**

For detailed setup instructions, see [SETUP_GUIDE.md](SETUP_GUIDE.md)
