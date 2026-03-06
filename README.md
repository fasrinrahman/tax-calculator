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
