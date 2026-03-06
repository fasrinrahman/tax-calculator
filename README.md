# 🇱🇰 Sri Lankan Tax Calculator (Python CLI)

A simple yet powerful **Python command-line application** that calculates personal income tax based on **Sri Lanka’s progressive tax brackets (April 2025 reforms)**.

This project demonstrates **clean Python programming**, **functional programming techniques**, and **financial calculation logic**, making it a great learning project for developers exploring **Python, algorithms, and CLI applications**.

---

## ✨ Features

- ✔ Progressive income tax calculation based on official Sri Lankan tax brackets  
- ✔ Calculates **effective tax rate (%)**  
- ✔ Computes **annual and monthly take-home salary**  
- ✔ Generates **detailed tax reports**  
- ✔ Ranks taxpayers by **tax paid**  
- ✔ Identifies **high-income earners** in the top tax bracket  
- ✔ Calculates **summary statistics** (total tax revenue, highest & lowest tax)

---

## 🧠 Concepts Demonstrated

This project showcases several **Python programming concepts**:

- Modular function design  
- Functional programming  
- Lambda expressions  
- Data processing and analysis  

### Python features used

- `map()` → apply tax calculation to multiple incomes  
- `filter()` → identify high-income taxpayers  
- `lambda` → inline functional operations  
- `zip()` → combine income and tax values  
- `sorted()` → rank taxpayers  
- Built-in functions (`sum`, `max`, `min`)

---

## 📊 Tax Brackets (Sri Lanka – April 2025)

| Annual Income (LKR) | Tax Rate |
|---------------------|---------|
| Up to 1,800,000 | 0% |
| 1,800,001 – 2,800,000 | 6% |
| 2,800,001 – 3,300,000 | 18% |
| 3,300,001 – 3,800,000 | 24% |
| 3,800,001 – 4,300,000 | 30% |
| Above 4,300,000 | 36% |

The calculator applies **progressive taxation**, meaning only the income within each bracket is taxed at that bracket’s rate.

---

## 🖥 Example Output
SRI LANKAN TAX CALCULATOR (April 2025 Tax Reforms)

Annual Income: Rs. 4,000,000
Income Tax: Rs. 330,000 (8.25%)
Take-Home (Annual): Rs. 3,670,000
Take-Home (Monthly): Rs. 305,833

TOP TAXPAYERS (Ranked by Tax Paid)

Rs. 5,000,000 - Tax Paid: Rs. 690,000

Rs. 4,000,000 - Tax Paid: Rs. 330,000

Rs. 3,500,000 - Tax Paid: Rs. 210,000


---

## ⚙️ Tech Stack

### Language
- 🐍 Python 3

### Concepts
- Functional Programming  
- Algorithm Design  
- Data Processing  
- Command Line Applications

---

## 📂 Project Structure
tax-calculator/
│
├── tax_calculator.py
└── README.md


### Main functions

- `calculate_income_tax()` → progressive tax calculation  
- `calculate_effective_tax_rate()` → tax percentage  
- `calculate_take_home()` → after-tax income  
- `main()` → runs tax reports and analysis

---

## 🚀 Possible Improvements

Future enhancements could include:

- Interactive user input  
- Web-based tax calculator  
- Export reports to **CSV / PDF**  
- Visual **tax charts**  
- Support for **multiple tax systems**

---

## 📚 Learning Goals

This project helps developers practice:

- Writing **clean Python functions**  
- Implementing **real-world financial algorithms**  
- Using **functional programming tools**  
- Structuring **CLI-based applications**

---

## ⭐ Contributing

Contributions, suggestions, and improvements are always welcome!  
Feel free to **fork the repository and submit a pull request**.

---

## 📄 License

This project is **open-source** and intended for **educational and learning purposes**.
