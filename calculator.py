"""A simple calculator module for basic math operations."""

from typing import Union


class Calculator:
    """Calculator class providing basic mathematical operations."""

    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b
        """
        return a + b

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Subtract second number from first number.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b
        """
        return a - b

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b
        """
        return a * b

    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Divide first number by second number.

        Args:
            a: Dividend
            b: Divisor

        Returns:
            Quotient of a and b

        Raises:
            ValueError: If divisor is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


if __name__ == "__main__":
    # Example usage
    calc = Calculator()
    
    print("=== Python Math Calculator ===")
    print(f"Addition: 5 + 3 = {calc.add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {calc.subtract(10, 4)}")
    print(f"Multiplication: 6 × 7 = {calc.multiply(6, 7)}")
    print(f"Division: 20 ÷ 4 = {calc.divide(20, 4)}")
    
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"Error: {e}")
