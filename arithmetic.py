"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of the two inputs."""

    sum = num1+num2
    return sum



def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    difference = num1 - num2
    return difference


def multiply(num1, num2):
    """Multiply the two inputs together."""

    product = num1 * num2
    return product


def divide(num1, num2):
    """Divide the first input by the second and return the result."""

    quotient = num1/num2
    return quotient


def square(num1):
    """Return the square of the input."""

    is_squared = num1 ** 2
    return is_squared


def cube(num1):
    """Return the cube of the input."""

    is_cubed = num1 ** 3
    return is_cubed


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    is_raised = num1 ** num2
    return is_raised


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    remainder = num1 % num2
    return remainder
