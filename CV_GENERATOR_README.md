# CV Test Data Generator

Generate test CV data in JSON format from an Excel skill matrix for automated testing and development.

## Features

- ✅ **Excel-based Input**: Read candidate skills from structured Excel file
- ✅ **Grouped Skill Format**: Skills organized by categories (資格・免許, 大学名)
- ✅ **Static Personal Data**: Consistent test data for reproducible testing
- ✅ **JSON Output**: Structured JSON with list_cv, jd, top_k, and custom_weights
- ✅ **Excel Export**: Automatically updates Excel with generated results
- ✅ **Flexible CLI**: Generate all CVs or specific candidates by index

## Quick Start

### Prerequisites

- **Python 3.11+**
- **openpyxl** library

### Installation

```bash
# Install dependencies
pip install openpyxl
```

### Usage

#### Generate All CVs

```bash
python utils/Test_data_generator.py data/data_matrix.xlsx -o data/cv_test_data.json
```

#### Generate Specific CV by Index

```bash
python utils/Test_data_generator.py data/data_matrix.xlsx -n 0
```

#### Skip Excel Update

```bash
python utils/Test_data_generator.py data/data_matrix.xlsx -o data/output.json --no-update
```

## Excel Structure

### Row 1: Category Headers (Merged Cells)
- **Columns A-E**: 資格・免許 (Certificates/Licenses)
- **Columns F-I**: 大学名 (University Names)

### Row 2: Skill Headers
Detailed skill names for each column

### Row 3+: Candidate Data
Mark skills with "x" for each candidate

### Example Excel Structure

| 資格・免許 | | | | | 大学名 | | | |
|---------|---|---|---|---|------|---|---|---|
| TOEIC | 英検準1級 | ... | ICTスキル | ... | 東京大学 | 広島大学 | 海外留学 | ... |
| x | | | x | | x | | | |
| | x | | | | | x | | |

## Output Structure

### JSON Format

```json
{
  "list_cv": [
    {
      "cv_id": "12788",
      "content": "氏名: 平林 直美\nフリガナ: ひらばやし なおみ\n性別: 女\n生年月日: 1977-07-20\n住所: 東京都国分寺市西恋ヶ窪2-8-11\n資格・免許: TOEIC, 英検準1級\n大学名: 東京大学, 広島大学\n"
    }
  ],
  "jd": {
    "content": "美術科 非常勤講師（中高一貫校）／勤務地: 東京都世田谷区／コマ数: 週13コマ／開始: 11月から\n必須: 中学・高校の美術教員免許。\n補足: ICT導入校。"
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

### CV Content Format

```
氏名: 平林 直美
フリガナ: ひらばやし なおみ
性別: 女
生年月日: 1977-07-20
住所: 東京都国分寺市西恋ヶ窪2-8-11
資格・免許: TOEIC, 英検準1級, ICTスキル活用授業に対応可能
大学名: 東京大学, 広島大学, 海外留学: 有り
```

**Key Features**:
- Skills grouped by category (資格・免許, 大学名)
- Comma-separated within each group
- Groups separated by newlines

## Excel Export

The generator automatically updates the Excel file with results:

- **Column Name**: "cv generated result"
- **Location**: Last column (Column J or 10)
- **Content**: CV ID, timestamp, and full CV content

## Static Data Configuration

The generator uses static personal information for consistent test data:

- **CV ID**: 12788
- **Name**: 平林 直美 (ひらばやし なおみ)
- **Gender**: 女
- **Birthdate**: 1977-07-20
- **Address**: 東京都国分寺市西恋ヶ窪2-8-11

To modify these values, edit the static constants in `utils/Test_data_generator.py`:

```python
class CVTestDataGenerator:
    STATIC_CV_ID = "12788"
    STATIC_NAME = "平林 直美"
    STATIC_FURIGANA = "ひらばやし なおみ"
    STATIC_BIRTHDATE = "1977-07-20"
    STATIC_GENDER = "女"
    STATIC_ADDRESS = "東京都国分寺市西恋ヶ窪2-8-11"
```

## Command-Line Options

```
usage: Test_data_generator.py [-h] [-o OUTPUT] [-n NUMBER] [--no-update] excel_file

Generate test CV data from Excel skill matrix

positional arguments:
  excel_file            Path to Excel file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output JSON file path (default: cv_test_data.json)
  -n NUMBER, --number NUMBER
                        Generate specific candidate by index (0-based)
  --no-update           Do not update Excel with generation results
```

## Project Structure

```
ist_automation_test/
├── data/
│   ├── data_matrix.xlsx       # Input Excel file with skill matrix
│   └── cv_test_data.json      # Generated JSON output
├── utils/
│   └── Test_data_generator.py # Main generator script
├── SETUP.md                   # Detailed Windows 11 setup guide
└── CV_GENERATOR_README.md     # This file
```

## Requirements

- **Python**: 3.11 or higher
- **Dependencies**:
  - openpyxl (3.0+)

Install dependencies:

```bash
pip install openpyxl
```

## Development

### Code Structure

The generator is implemented as a single Python class:

```python
class CVTestDataGenerator:
    - load_excel()              # Read Excel file and headers
    - extract_candidate_skills() # Extract skills from candidate row
    - build_cv_content()        # Build formatted CV content
    - generate_single_cv()      # Generate one CV
    - generate_all_cvs()        # Generate all CVs
    - generate_cv_by_index()    # Generate CV by index
```

### Extending the Generator

To add new static fields:

1. Add constants to the class
2. Update `build_cv_content()` method
3. Regenerate test data

To modify skill grouping:

1. Update `category_headers` in `load_excel()`
2. Modify `extract_candidate_skills()` extraction logic
3. Update `build_cv_content()` formatting

## Troubleshooting

### Common Issues

**Problem**: "No module named 'openpyxl'"
```bash
pip install openpyxl
```

**Problem**: Excel file not updating
- Close Excel before running the generator
- Check file permissions (not read-only)
- Run with administrator privileges if needed

**Problem**: 0 CVs generated
- Verify Excel structure (Row 1: categories, Row 2: skills, Row 3+: data)
- Ensure at least one "x" mark exists in candidate rows
- Check that data starts from Row 3

**Problem**: Japanese characters not displaying
- Use UTF-8 compatible text editor (VS Code, Notepad++)
- Verify Excel encoding settings

## Windows 11 Setup

For detailed setup instructions on a fresh Windows 11 PC with no Python installed, see **[SETUP.md](SETUP.md)**

The setup guide includes:
- Python installation from scratch
- Git installation and repository cloning
- Dependency installation
- Complete troubleshooting guide
- Quick reference for common commands

---

**Last Updated**: 2025-11-06
**Python Version**: 3.11+
**Documentation**: See SETUP.md for complete Windows 11 setup instructions
