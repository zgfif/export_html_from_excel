# Excel to HTML Converter

This app extracts HTML code from an Excel sheet and creates corresponding HTML files.  
It can also replace links extracted from another Excel file.

## Prerequisites

- Installed **Python** (latest stable version recommended)
- Installed **venv** module (for creating virtual environments)
- Installed **pip** (for installing dependencies)


## Installation and Usage

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
   
on Linux/macOS:
```bash 
source .venv/bin/activate 
```   
on Windows:
```powershell
.venv\Scripts\Activate.ps1
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash 
python main.py
```

## Running Tests
```bash
python -m unittest discover tests/
```

