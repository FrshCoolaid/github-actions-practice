"""
Simple calculator module for demonstration.
"""

def add(a, b):
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
        
    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
    """
    return a + b


def subtract(a, b):
    """Subtract b from a.
    
    Args:
        a: Number to subtract from
        b: Number to subtract
        
    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a, b):
    """Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
    """
    return a * b


def divide(a, b):
    """Divide a by b.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Quotient of a and b
        
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    """Raise base to the power of exponent.
    
    Args:
        base: The base number
        exponent: The exponent
        
    Returns:
        base raised to the power of exponent
    """
    return base ** exponent