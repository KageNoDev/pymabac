
MABAC Decision Support App
===========================

This is a Python-based desktop GUI application for performing MABAC (Multi-Attributive Border Approximation area Comparison)
decision-making analysis with integrated sensitivity analysis and visualizations.

🚀 Features
-----------
- Load decision matrix from CSV or TXT files
- Define custom weights and criteria types (benefit/cost)
- Run MABAC algorithm to compute rankings
- Perform sensitivity analysis by removing criteria one-by-one
- View results in text and charts
- Export generated plots (PNG, JPG, PDF)

🛠 Installation
---------------
Clone the repository and install it in editable mode:

```
git clone https://github.com/KageNoDev/mabac-app.git
cd mabac-app
pip install -e .
```

> Requires Python 3.7 or later.

▶️ Usage
--------
After installation, launch the GUI by running:

```
mabac-gui
```

Or directly via:

```
python main.py
```

🧠 Input Format
---------------
- Decision Matrix: CSV/TXT file with numerical values.
- Weights: Comma-separated (e.g., 0.2,0.3,0.5)
- Criteria Types: Comma-separated binary (e.g., 1,0,1)
    - 1 → Benefit (higher = better)
    - 0 → Cost (lower = better)

✅ Example
----------
Matrix:
```
3,4,2
2,5,3
4,3,1
```

Weights:
```
0.3,0.4,0.3
```

Criteria Types:
```
1,1,0
```

🧪 Running Tests
----------------
```
pytest tests/
```

📦 Package Structure
--------------------
```
mabac_app/
├── mabac/                  # Core logic (MABAC, metrics, analysis)
├── main.py                 # GUI application
├── tests/                  # Unit tests
├── setup.py                # Install script
└── README.md
```

📚 License
----------
MIT License

👤 Author
---------
Created by [Laura Białobrzewska] – feel free to contribute or fork!
