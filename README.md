# FavQsAPIv2 Testing Project

This project contains automated API tests for the FavQs public API.  
Tests are written in Python using `requests`, `pytest`, and `faker`.

---

# Project Setup

## 1. Clone the repo:

```bash
git clone https://github.com/yourusername/FavQsAPIv2.git
cd FavQsAPIv2
```

## 2. Create and activate a virtual environment:

**Windows:**
```bash
python -m venv FavQsAPIv2
.\FavQsAPIv2\Scripts\Activate.ps1
```

**Bash in VSCode (Windows):**
```bash
source FavQsAPIv2/Scripts/activate
```

**Linux/MacOS:**
```bash
python3 -m venv FavQsAPIv2
source FavQsAPIv2/bin/activate
```

## 3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 4. Running Tests

**Running All Tests:**
```bash
python -m pytest -v
# or
pytest -v
```

**Running Tests with print output:**
```bash
pytest -v -s
```

**Running specific case in test with print output:**
```bash
pytest -v -s test_name.py::name-of-the-case
```
