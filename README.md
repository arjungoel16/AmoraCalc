#AmoraCalc
        AmoraCalc is a modular, test-driven Python tool that combines real-world loan payment calculations with recursive mathematical functions like Fibonacci and Factorial. This project is designed to serve both practical and educational purposes — helping users understand financial amortization while exploring how recursive algorithms work under the hood.
        🔍 Features
        •	📈 Loan Amortization Calculator
          - Computes detailed monthly payment schedules
          - Supports 0% and non-zero interest rates
          - Outputs breakdown of principal and interest for each month
        •	🔁 Recursive Fibonacci Calculator
          - Educational tool to illustrate how recursion builds the Fibonacci sequence
          - Strict input validation with time complexity annotation
          - Great for teaching recursion and exponential growth patterns
        •	🧮 Recursive Factorial Calculator
          - Simple recursive implementation
          - Edge-case handling and type safety
        •	✅ Full Pytest-Based Test Suite
          - Unit tests for all functions
          - Includes edge cases and error handling scenarios
          - Great reference for writing robust Python test code
        🧠 Educational Value
        While the loan calculator provides immediate practical value, this project intentionally includes a recursive implementation of the Fibonacci sequence to help students and developers visualize how recursion works — including the trade-offs in performance and how exponential growth occurs in recursive call stacks.
        
    - Time complexity of Fibonacci: O(2ⁿ) (naive recursion)
    - Demonstrates the need for memoization or dynamic programming
    - Ideal for introductory CS or algorithm courses
    📁 Project Structure
    AmoraCalc/
    ├── loans.py           # Core logic: loan calculator, fibonacci, factorial
    ├── unit_tests.py      # Unit tests using pytest
    ├── README.md               # This file
    🚀 Getting Started
    Requirements:
    - Python 3.7+
    - pytest for testing
    Install pytest:
      pip install pytest
    Run Unit Tests:
      pytest test_loan_utils.py -v
    Example Usage:
      from loan_utils import calculate_loan_schedule, fibonacci, factorial
    
      print(fibonacci(7))  # Output: 13
    
      schedule = calculate_loan_schedule(1200, 6, 1)
      for month in schedule:
          print(month)
    💡 Future Enhancements
    •	Memoized Fibonacci version for large inputs
    •	Streamlit GUI for interactive user experience
    •	CSV export for loan schedules
    •	Performance benchmarking for recursive vs optimized solutions
    🏁 License
    This project is open-source and free to use under the MIT License.
    👨‍🏫 Author
    Arjun
    Educational developer & software engineer passionate about making algorithms and finance accessible through code.
