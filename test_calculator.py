"""Unit tests for the calculator module."""

import pytest
from calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(10, 20) == 30

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert self.calc.add(-5, -3) == -8
        assert self.calc.add(-10, 5) == -5

    def test_add_floats(self):
        """Test addition of floating-point numbers."""
        assert self.calc.add(3.5, 2.5) == 6.0
        assert self.calc.add(1.1, 2.2) == pytest.approx(3.3)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert self.calc.subtract(10, 4) == 6
        assert self.calc.subtract(20, 15) == 5

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        assert self.calc.subtract(-5, -3) == -2
        assert self.calc.subtract(10, -5) == 15

    def test_subtract_floats(self):
        """Test subtraction of floating-point numbers."""
        assert self.calc.subtract(5.5, 2.5) == 3.0
        assert self.calc.subtract(10.5, 3.2) == pytest.approx(7.3)

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert self.calc.multiply(6, 7) == 42
        assert self.calc.multiply(5, 5) == 25

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert self.calc.multiply(-3, 4) == -12
        assert self.calc.multiply(-5, -5) == 25

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert self.calc.multiply(10, 0) == 0
        assert self.calc.multiply(0, 10) == 0

    def test_multiply_floats(self):
        """Test multiplication of floating-point numbers."""
        assert self.calc.multiply(2.5, 4) == 10.0
        assert self.calc.multiply(1.5, 2.5) == pytest.approx(3.75)

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert self.calc.divide(20, 4) == 5.0
        assert self.calc.divide(15, 3) == 5.0

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert self.calc.divide(-20, 4) == -5.0
        assert self.calc.divide(-15, -3) == 5.0

    def test_divide_floats(self):
        """Test division of floating-point numbers."""
        assert self.calc.divide(10.5, 2) == 5.25
        assert self.calc.divide(7.5, 2.5) == pytest.approx(3.0)

    def test_divide_by_zero(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)

    def test_divide_zero_by_number(self):
        """Test division of zero by a number."""
        assert self.calc.divide(0, 10) == 0.0
