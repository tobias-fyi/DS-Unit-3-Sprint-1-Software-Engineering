"""A series of functions for calculating the square root."""

def lazy_sqrt(x):
    """The simplest way to do square root. Take the 1/2 power."""
    return x**0.5

def builtin_sqrt(x):
    """Use the math library to get the square root."""
    from math import sqrt
    return sqrt(x)

def newton_sqrt(x):
    """Uses the Newton method to return square root."""
    val = x
    while True:
        last = val
        val = (val + x /val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val
