# 🚀 AmoraCalc

**AmoraCalc** is a modular, test-driven Python tool that combines real-world **loan payment calculations** with recursive **mathematical functions** like **Fibonacci** and **Factorial**.

This project is ideal for developers, students, and educators who want to understand how amortization schedules are calculated and how recursive algorithms (especially Fibonacci) behave in Python.

---

## 🔍 Features

- 📈 **Loan Amortization Calculator**
  - Computes monthly payment breakdowns
  - Supports both 0% and non-zero interest rates
  - Outputs principal, interest, and remaining balance per month

- 🔁 **Recursive Fibonacci Calculator**
  - Pure recursive implementation
  - Educational: Demonstrates exponential call growth
  - Includes input validation and complexity notes

- 🧮 **Recursive Factorial Calculator**
  - Simple, clean recursive approach
  - Edge-case handling and input validation

- ✅ **Unit Tested with Pytest**
  - Full coverage for edge cases, invalid inputs, and base cases
  - Teaches how to write clean, readable tests

---

## 🧠 Educational Value

This project intentionally includes a recursive Fibonacci function to:

- Demonstrate recursion structure and exponential time complexity `O(2^n)`
- Encourage deeper understanding of performance bottlenecks
- Serve as a base for exploring optimization (e.g. memoization)

> Perfect for CS101 and algorithm visualization lessons.

---

## 📁 Project Structure

```
AmoraCalc/
├── loans.py           # Core logic: loan calculator, fibonacci, factorial
├── unit_tests.py      # Unit tests using pytest
├── README.md               # Project documentation
```

---

## 🛠️ Getting Started

### Requirements

- Python 3.7+
- `pytest` for running unit tests

### Install Pytest

```bash
pip install pytest
```

### Run Unit Tests

```bash
pytest test_loans.py -v
```

### Example Usage

```python
from loans import calculate_loan_schedule, fibonacci, factorial

# Recursive Fibonacci
print(fibonacci(7))  # Output: 13

# Factorial
print(factorial(5))  # Output: 120

# Loan Payment Schedule
schedule = calculate_loan_schedule(1200, 6, 1)
for month in schedule:
    print(month)
```

---

## 📊 Sample Output

```
Month | Payment | Principal | Interest | Balance
-------------------------------------------------
   1  | 103.32  |   97.32   |   6.00   | 1102.68
   2  | 103.32  |   97.81   |   5.51   | 1004.87
  ...
```

---

## 💡 Future Enhancements

- Add memoized Fibonacci version
- Build a Streamlit dashboard
- Export amortization schedule to CSV
- Add performance benchmarking tools

---

## 🏁 License

MIT License — Free to use and modify.

---

## 👨‍🏫 Author

**Arjun**  
Educational developer & software engineer passionate about making algorithms and finance accessible through code.
