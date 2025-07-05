# 🧠 LeetCode Python Solutions

**By Eric Li**

This repository contains my personal Python solutions to LeetCode problems.  
Each solution is cleanly structured and accompanied by unit tests written using [`pytest`](https://docs.pytest.org/).  
The project is organized for easy navigation, consistent naming, and reproducibility.

---

## 📁 Directory Structure

```
leetcode-solutions/
├── solutions/               # Python implementations
│   ├── problem_XXXX_name_of_problem.py
│   └── ...
├── tests/                   # pytest test cases
│   ├── test_problem_XXXX_name_of_problem.py
│   └── ...
├── utils/
│   └── tree_utils.py        # Binary tree helpers
├── requirements.txt         # Dependencies (pytest, etc.)
├── pytest.ini               # Pytest config file
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

### 1. Create and Activate a Virtual Environment

```bash
# macOS/Linux
python -m venv venv
source venv/bin/activate        
```

```bash
# Windows
python -m venv venv
venv\Scripts\activate           
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Tests

```bash
pytest
```

---

## 📜 License

This project is for personal and educational use only.  
Problem descriptions are © [LeetCode](https://leetcode.com), included here under fair use.

---
