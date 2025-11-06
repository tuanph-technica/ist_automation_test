# Setup Guide - IST Automation Test Framework

Complete step-by-step setup guide for the automation testing framework.

## 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Python Installation](#python-installation)
3. [Project Setup](#project-setup)
4. [Browser Driver Setup](#browser-driver-setup)
5. [Environment Configuration](#environment-configuration)
6. [Verification](#verification)
7. [IDE Setup](#ide-setup)
8. [Troubleshooting](#troubleshooting)

---

## 1. System Requirements

### Minimum Requirements

- **Operating System**: Windows 10/11, macOS 10.14+, Linux (Ubuntu 18.04+)
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Disk Space**: 500MB for dependencies
- **Browser**: Chrome 90+, Firefox 88+, or Edge 90+

### Check Existing Installation

```bash
# Check Python version
python --version
# or
python3 --version

# Check pip version
pip --version
# or
pip3 --version
```

---

## 2. Python Installation

### Windows

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run installer
3. ✅ Check "Add Python to PATH"
4. Click "Install Now"
5. Verify installation:
   ```bash
   python --version
   pip --version
   ```

### macOS

**Using Homebrew** (recommended):
```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.11

# Verify
python3 --version
pip3 --version
```

**Using Official Installer**:
1. Download from [python.org](https://www.python.org/downloads/)
2. Run .pkg installer
3. Follow installation wizard

### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip python3-venv

# Verify
python3 --version
pip3 --version
```

---

## 3. Project Setup

### Step 1: Navigate to Project Directory

```bash
cd /path/to/ist_automation_test
```

### Step 2: Create Virtual Environment

**Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### Step 3: Upgrade pip

```bash
pip install --upgrade pip
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- selenium
- pytest
- webdriver-manager
- And all other required packages

### Step 5: Verify Installation

```bash
pip list
```

Check that all packages from `requirements.txt` are installed.

---

## 4. Browser Driver Setup

### Automatic Setup (Recommended)

The framework uses `webdriver-manager` to automatically download and manage browser drivers. No manual setup required!

### Manual Setup (Optional)

If you prefer manual driver management:

#### Chrome Driver

1. Check Chrome version: `chrome://version`
2. Download matching driver from [chromedriver.chromium.org](https://chromedriver.chromium.org/)
3. Place in `drivers/` directory
4. Make executable (macOS/Linux):
   ```bash
   chmod +x drivers/chromedriver
   ```

#### Firefox Driver (geckodriver)

1. Check Firefox version: Menu → Help → About Firefox
2. Download from [github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
3. Place in `drivers/` directory
4. Make executable (macOS/Linux):
   ```bash
   chmod +x drivers/geckodriver
   ```

#### Edge Driver

1. Check Edge version: `edge://version`
2. Download from [developer.microsoft.com/microsoft-edge/tools/webdriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
3. Place in `drivers/` directory

---

## 5. Environment Configuration

### Step 1: Copy Environment Template

```bash
cp .env.example .env
```

### Step 2: Edit Configuration

Open `.env` file and configure:

```env
# Environment
ENV=dev

# Application URLs - CHANGE THESE
BASE_URL=https://your-actual-app-url.com
API_BASE_URL=https://api.your-actual-app-url.com

# Browser Configuration
BROWSER=chrome              # chrome, firefox, edge
HEADLESS=false             # Set to true for headless mode
IMPLICIT_WAIT=10
EXPLICIT_WAIT=20
PAGE_LOAD_TIMEOUT=30

# Test Credentials - CHANGE THESE
TEST_USER_EMAIL=your-test-user@example.com
TEST_USER_PASSWORD=YourTestPassword123

# Reporting
GENERATE_ALLURE_REPORT=true
SCREENSHOT_ON_FAILURE=true

# Parallel Execution
PARALLEL_WORKERS=4
```

### Step 3: Create Required Directories

```bash
mkdir -p reports logs data/screenshots drivers
```

---

## 6. Verification

### Test Framework Installation

```bash
# Check pytest
pytest --version

# Check selenium
python -c "import selenium; print(selenium.__version__)"
```

### Run Sample Test

```bash
# Run a simple test to verify everything works
pytest tests/test_cases/test_sample_login.py::TestLogin::test_remember_me_functionality -v
```

### Expected Output

```
========================= test session starts =========================
collected 1 item

tests/test_cases/test_sample_login.py::TestLogin::test_remember_me_functionality PASSED

========================= 1 passed in 5.23s =========================
```

### Run All Tests (Dry Run)

```bash
pytest --collect-only
```

This will show all discovered tests without running them.

---

## 7. IDE Setup

### Visual Studio Code

1. **Install Python Extension**
   - Open Extensions (Ctrl+Shift+X)
   - Search "Python"
   - Install official Microsoft Python extension

2. **Configure Python Interpreter**
   - Press Ctrl+Shift+P
   - Type "Python: Select Interpreter"
   - Choose the venv interpreter: `./venv/bin/python`

3. **Install Recommended Extensions**
   - Python Test Explorer
   - Python Docstring Generator
   - GitLens

4. **Workspace Settings** (`.vscode/settings.json`)
   ```json
   {
     "python.testing.pytestEnabled": true,
     "python.testing.unittestEnabled": false,
     "python.testing.pytestArgs": ["-v"],
     "python.linting.enabled": true,
     "python.linting.pylintEnabled": true
   }
   ```

### PyCharm

1. **Configure Python Interpreter**
   - File → Settings → Project → Python Interpreter
   - Add Interpreter → Existing Environment
   - Select `venv/bin/python` (or `venv\Scripts\python.exe` on Windows)

2. **Configure pytest**
   - File → Settings → Tools → Python Integrated Tools
   - Default test runner: pytest

3. **Run Configuration**
   - Right-click on `tests/` directory
   - "Run 'pytest in tests'"

---

## 8. Troubleshooting

### Issue: Module Not Found

```bash
# Ensure virtual environment is activated
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: WebDriver Not Found

```bash
# Clear WebDriver cache
rm -rf ~/.wdm  # macOS/Linux
rmdir /s %USERPROFILE%\.wdm  # Windows

# Let webdriver-manager download fresh drivers
pytest tests/test_cases/test_sample_login.py -k test_remember_me_functionality
```

### Issue: Permission Denied (Linux/macOS)

```bash
# Make drivers executable
chmod +x drivers/*

# Or run with sudo for system-wide installation
sudo python -m pytest
```

### Issue: Browser Version Mismatch

```bash
# Update webdriver-manager
pip install --upgrade webdriver-manager

# Clear cache
rm -rf ~/.wdm
```

### Issue: Tests Not Discovered

```bash
# Check pytest configuration
pytest --collect-only -v

# Ensure you're in project root directory
pwd  # Should show .../ist_automation_test

# Check Python path
python -c "import sys; print('\n'.join(sys.path))"
```

### Issue: Import Errors

```bash
# Add project root to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"  # Linux/macOS
set PYTHONPATH=%PYTHONPATH%;%cd%  # Windows

# Or install project in editable mode
pip install -e .
```

### Common Environment Issues

**Symptom**: Tests connect to wrong environment

**Solution**:
1. Verify `.env` file exists and is in project root
2. Check `BASE_URL` in `.env`
3. Use command line override:
   ```bash
   pytest --env=staging
   ```

### Debugging Failed Tests

1. **Enable verbose logging**:
   ```bash
   pytest -v --log-cli-level=DEBUG
   ```

2. **Run single test with output**:
   ```bash
   pytest tests/test_cases/test_sample_login.py::TestLogin::test_valid_login -v -s
   ```

3. **Check screenshots**:
   - Location: `reports/screenshots/`
   - Automatic on test failure

4. **Review logs**:
   - Location: `logs/test_execution.log`

---

## ✅ Setup Complete!

Your test automation framework is ready to use.

### Next Steps

1. ✏️ Update page objects for your application
2. ✏️ Create new test cases
3. 🏃 Run your first test suite
4. 📊 Review HTML reports

### Quick Commands Reference

```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Run all tests
pytest

# Run with HTML report
pytest --html=reports/report.html

# Run specific markers
pytest -m smoke

# Run in parallel
pytest -n auto

# Run with different browser
pytest --browser=firefox
```

---

**Need Help?** Check the main [README.md](README.md) or contact the QA team.
