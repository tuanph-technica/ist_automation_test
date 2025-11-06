# CV Test Data Generator - Windows 11 Setup Guide

Complete setup instructions for a fresh Windows 11 PC with no Python installation.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installing Python](#installing-python)
3. [Getting the Code](#getting-the-code)
4. [Installing Dependencies](#installing-dependencies)
5. [Verifying Installation](#verifying-installation)
6. [Running the Generator](#running-the-generator)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Software
- **Windows 11** (any edition)
- **Git for Windows** (for cloning from GitHub)
- **Internet connection** (for downloading Python and dependencies)

### Recommended Tools
- **Windows Terminal** (optional, but provides better experience)
- **Visual Studio Code** (optional, for viewing/editing code)

---

## Installing Python

### Step 1: Download Python

1. Open your web browser
2. Go to: https://www.python.org/downloads/
3. Click the **"Download Python 3.11.x"** button (or latest 3.11+ version)
4. Save the installer to your Downloads folder

### Step 2: Install Python

1. **Run the installer** (double-click the downloaded file)
2. **IMPORTANT**: Check the box **"Add Python to PATH"** at the bottom
3. Click **"Install Now"**
4. Wait for installation to complete
5. Click **"Close"** when finished

### Step 3: Verify Python Installation

1. Press `Win + R` to open Run dialog
2. Type `cmd` and press Enter
3. In the command prompt, type:
   ```cmd
   python --version
   ```
4. You should see: `Python 3.11.x` (or similar)
5. Type:
   ```cmd
   pip --version
   ```
6. You should see: `pip 23.x.x from ...`

**If you don't see the versions**, restart your computer and try again.

---

## Getting the Code

### Option A: Using Git (Recommended)

#### Install Git for Windows

1. Go to: https://git-scm.com/download/win
2. Download the 64-bit installer
3. Run the installer with default settings
4. Click "Next" through all prompts
5. Click "Finish"

#### Clone the Repository

1. Open **Command Prompt** or **Windows Terminal**
2. Navigate to where you want to store the project:
   ```cmd
   cd C:\Users\YourUsername\Documents
   ```
3. Clone the repository:
   ```cmd
   git clone https://github.com/YOUR_USERNAME/ist_automation_test.git
   ```
4. Navigate into the project folder:
   ```cmd
   cd ist_automation_test
   ```

### Option B: Download ZIP from GitHub

1. Go to the GitHub repository in your browser
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. Extract the ZIP file to a location like:
   ```
   C:\Users\YourUsername\Documents\ist_automation_test
   ```
5. Open **Command Prompt** and navigate to the folder:
   ```cmd
   cd C:\Users\YourUsername\Documents\ist_automation_test
   ```

---

## Installing Dependencies

### Step 1: Open Command Prompt in Project Folder

1. Open **File Explorer**
2. Navigate to the project folder: `ist_automation_test`
3. Click in the address bar at the top
4. Type `cmd` and press Enter
   - This opens Command Prompt in the project folder

### Step 2: Install Required Python Packages

Run the following command:

```cmd
pip install openpyxl
```

**Expected Output:**
```
Collecting openpyxl
  Downloading openpyxl-3.x.x-py2.py3-none-any.whl
Installing collected packages: et-xmlfile, openpyxl
Successfully installed et-xmlfile-1.x.x openpyxl-3.x.x
```

### Step 3: Verify Installation

```cmd
pip list
```

You should see:
```
Package      Version
------------ -------
openpyxl     3.x.x
et-xmlfile   1.x.x
pip          23.x.x
setuptools   xx.x.x
```

---

## Verifying Installation

### Check Project Structure

Make sure you have the following files and folders:

```
ist_automation_test/
├── data/
│   └── data_matrix.xlsx       ← Excel input file
├── utils/
│   └── Test_data_generator.py ← Main Python script
└── README.md (or SETUP.md)
```

### Test the Script

Run a quick test to ensure everything works:

```cmd
python utils\Test_data_generator.py data\data_matrix.xlsx -o data\test_output.json
```

**Expected Output:**
```
Generated 14 CV records
Saved to: data\test_output.json
Updated Excel file: data\data_matrix.xlsx

Example (first CV):
{
  "cv_id": "12788",
  "content": "氏名: 平林 直美\n..."
}
```

---

## Running the Generator

### Basic Usage

```cmd
python utils\Test_data_generator.py data\data_matrix.xlsx -o data\cv_test_data.json
```

This will:
- ✅ Read the Excel file: `data\data_matrix.xlsx`
- ✅ Generate CV test data
- ✅ Save JSON output to: `data\cv_test_data.json`
- ✅ Update Excel with results in the last column

### Command Options

#### Generate All CVs (Default)
```cmd
python utils\Test_data_generator.py data\data_matrix.xlsx -o data\output.json
```

#### Generate Specific CV by Index
```cmd
python utils\Test_data_generator.py data\data_matrix.xlsx -n 0
```
- `-n 0` = First candidate (0-based index)
- `-n 5` = Sixth candidate

#### Skip Excel Update
```cmd
python utils\Test_data_generator.py data\data_matrix.xlsx -o data\output.json --no-update
```

#### Show Help
```cmd
python utils\Test_data_generator.py --help
```

---

## Understanding the Output

### JSON Structure

The generated JSON file has this structure:

```json
{
  "list_cv": [
    {
      "cv_id": "12788",
      "content": "氏名: 平林 直美\nフリガナ: ひらばやし なおみ\n..."
    }
  ],
  "jd": {
    "content": "美術科 非常勤講師（中高一貫校）..."
  },
  "top_k": 1,
  "custom_weights": {
    "license_score": 0.4,
    "hours_score": 0.2,
    "reliability_score": 0.2,
    "competency_score": 0.2
  }
}
```

### Excel Results

The Excel file will be updated with a new column:
- **Column Name**: "cv generated result"
- **Location**: Last column (Column J or 10)
- **Content**: Full CV data with CV ID and timestamp

---

## Troubleshooting

### Problem: "python is not recognized as an internal or external command"

**Solution:**
1. Reinstall Python and make sure to check **"Add Python to PATH"**
2. Or manually add Python to PATH:
   - Search for "Environment Variables" in Windows
   - Edit "Path" under System Variables
   - Add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311`
   - Add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\Scripts`
3. Restart Command Prompt or computer

### Problem: "No module named 'openpyxl'"

**Solution:**
```cmd
pip install openpyxl
```

If that fails:
```cmd
python -m pip install --upgrade pip
python -m pip install openpyxl
```

### Problem: "Permission denied" when saving files

**Solution:**
1. Close Excel if the file is open
2. Run Command Prompt as Administrator:
   - Right-click Command Prompt
   - Select "Run as administrator"
3. Make sure the files are not read-only:
   - Right-click the file
   - Properties → Uncheck "Read-only"

### Problem: Excel file is corrupted or won't open

**Solution:**
1. Make a backup of your original Excel file
2. Open Excel and repair the file:
   - File → Open → Browse
   - Select the file
   - Click the arrow next to "Open"
   - Choose "Open and Repair"

### Problem: Japanese characters not displaying correctly

**Solution:**
1. Make sure Excel is set to UTF-8 encoding
2. Open the JSON file with a text editor that supports UTF-8:
   - Notepad++ (download from: https://notepad-plus-plus.org/)
   - Visual Studio Code (download from: https://code.visualstudio.com/)

### Problem: Script runs but generates 0 CVs

**Solution:**
1. Check that `data\data_matrix.xlsx` exists
2. Verify the Excel structure:
   - Row 1: Merged category headers (資格・免許, 大学名)
   - Row 2: Skill headers
   - Row 3+: Candidate data with "x" marks
3. Ensure at least one candidate row has at least one "x" mark

---

## Quick Reference

### File Locations
- **Script**: `utils\Test_data_generator.py`
- **Input Excel**: `data\data_matrix.xlsx`
- **Output JSON**: `data\cv_test_data.json` (or custom name)
- **Updated Excel**: `data\data_matrix.xlsx` (Column J)

### Common Commands

```cmd
# Generate all CVs
python utils\Test_data_generator.py data\data_matrix.xlsx -o data\output.json

# Generate specific CV (index 0)
python utils\Test_data_generator.py data\data_matrix.xlsx -n 0

# Skip Excel update
python utils\Test_data_generator.py data\data_matrix.xlsx -o data\output.json --no-update

# Show help
python utils\Test_data_generator.py --help
```

---

## Additional Resources

### Python Documentation
- Official Python Tutorial: https://docs.python.org/3/tutorial/
- pip Documentation: https://pip.pypa.io/en/stable/

### openpyxl Documentation
- Official Documentation: https://openpyxl.readthedocs.io/

### Windows Command Prompt Basics
- `cd` - Change directory
- `dir` - List files in current directory
- `cd..` - Go up one directory
- `cls` - Clear screen
- `exit` - Close Command Prompt

---

## Support

If you encounter any issues not covered in this guide:

1. Check that Python and openpyxl are installed correctly
2. Verify the Excel file structure matches the expected format
3. Make sure you're running commands from the correct directory
4. Try running Command Prompt as Administrator

---

**Last Updated**: 2025-11-06
**Python Version**: 3.11+
**Operating System**: Windows 11
