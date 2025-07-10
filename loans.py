
"""
Loan Utility Functions
----------------------
This module provides utility functions for financial calculations and recursion-based math helpers.

Features:
- Monthly loan payment schedule with interest
- Recursive factorial calculator
- Recursive Fibonacci calculator

All functions are tested via pytest.
"""

def factorial(n):
    """
    Recursively calculates the factorial of n.

    Parameters:
    n (int): Non-negative integer.

    Returns:
    int: n!

    Raises:
    ValueError: If n is negative.
    TypeError: If n is not an integer.

    Time Complexity:
    O(n)
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input cannot be negative")
    return 1 if n == 0 else n * factorial(n - 1)

def fibonacci(n):
    """
    Recursively calculates the nth Fibonacci number.

    Parameters:
    n (int): Non-negative integer index in the Fibonacci sequence.

    Returns:
    int: The nth Fibonacci number.

    Raises:
    ValueError: If n is negative.
    TypeError: If n is not an integer.

    Time Complexity:
    O(2^n)
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input cannot be negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def calculate_loan_schedule(principal, annual_rate, years):
    """
    Calculates a monthly loan amortization schedule.

    Parameters:
    principal (float): Initial loan amount.
    annual_rate (float): Annual interest rate as a percentage.
    years (int): Loan term in years.

    Returns:
    list of tuples: Each tuple contains (month, payment, principal_paid, interest_paid, remaining_balance)

    Raises:
    ValueError: If inputs are invalid.

    Time Complexity:
    O(n), where n = years * 12
    """
    if principal < 0 or annual_rate < 0 or years <= 0:
        raise ValueError("Invalid loan input values")

    monthly_rate = annual_rate / 12 / 100
    months = years * 12

    if monthly_rate == 0:
        payment = principal / months
    else:
        payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)

    schedule = []
    for month in range(1, months + 1):
        interest = principal * monthly_rate
        principal_payment = payment - interest
        principal -= principal_payment
        schedule.append((
            month,
            round(payment, 2),
            round(principal_payment, 2),
            round(interest, 2),
            round(principal, 2)
        ))
    return schedule
