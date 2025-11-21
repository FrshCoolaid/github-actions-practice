"""
Tests for calculator module.
"""

import pytest
from src.calculator import add, subtract, multiply, divide, power


class TestAddition:
    """Tests for add function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-5, -3) == -8
        assert add(-10, -1) == -11
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(10, -5) == 5
        assert add(-10, 5) == -5
    
    def test_add_zero(self):
        """Test adding zero."""
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 5) == 5
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)


class TestSubtraction:
    """Tests for subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(10, 5) == 5
        assert subtract(20, 8) == 12
    
    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative."""
        assert subtract(5, 10) == -5
    
    def test_subtract_zero(self):
        """Test subtracting zero."""
        assert subtract(10, 0) == 10
        assert subtract(0, 10) == -10


class TestMultiplication:
    """Tests for multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(3, 4) == 12
        assert multiply(7, 8) == 56
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-3, 4) == -12
        assert multiply(-3, -4) == 12


class TestDivision:
    """Tests for divide function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5
        assert divide(20, 4) == 5
    
    def test_divide_with_remainder(self):
        """Test division with remainder."""
        assert divide(10, 3) == pytest.approx(3.333, rel=1e-2)
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
    
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0


class TestPower:
    """Tests for power function."""
    
    def test_power_positive_exponent(self):
        """Test raising to positive power."""
        assert power(2, 3) == 8
        assert power(5, 2) == 25
    
    def test_power_zero_exponent(self):
        """Test raising to power of zero."""
        assert power(5, 0) == 1
        assert power(100, 0) == 1
    
    def test_power_negative_exponent(self):
        """Test raising to negative power."""
        assert power(2, -1) == 0.5
        assert power(10, -2) == 0.01