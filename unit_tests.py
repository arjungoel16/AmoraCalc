
"""
Unit Tests for Loan Utility Functions
-------------------------------------
Tests all core logic:
- Factorial recursion
- Fibonacci recursion
- Loan amortization schedule
"""

import pytest
from loans import factorial, fibonacci, calculate_loan_schedule

# ---- Factorial Tests ----

def test_factorial_basic():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_factorial_large():
    assert factorial(7) == 5040

def test_factorial_type_error():
    with pytest.raises(TypeError):
        factorial("ten")  # type: ignore

def test_factorial_value_error():
    with pytest.raises(ValueError):
        factorial(-4)

# ---- Fibonacci Tests ----

def test_fibonacci_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_typical():
    assert fibonacci(5) == 5
    assert fibonacci(7) == 13
    assert fibonacci(10) == 55

def test_fibonacci_type_error():
    with pytest.raises(TypeError):
        fibonacci(5.5)
    with pytest.raises(TypeError):
        fibonacci("eight")  # type: ignore

def test_fibonacci_value_error():
    with pytest.raises(ValueError):
        fibonacci(-1)

# ---- Loan Calculation Tests ----

def test_loan_schedule_no_interest():
    schedule = calculate_loan_schedule(1200, 0, 1)
    assert len(schedule) == 12
    assert all(abs(month[1] - 100.0) < 1e-2 for month in schedule)

def test_loan_schedule_typical():
    schedule = calculate_loan_schedule(1000, 12, 1)
    assert len(schedule) == 12
    assert all(month[3] > 0 for month in schedule)  # Interest > 0

def test_loan_schedule_invalid_inputs():
    with pytest.raises(ValueError):
        calculate_loan_schedule(-1000, 5, 1)
    with pytest.raises(ValueError):
        calculate_loan_schedule(1000, -5, 1)
    with pytest.raises(ValueError):
        calculate_loan_schedule(1000, 5, 0)
