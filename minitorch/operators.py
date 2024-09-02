"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

# Implementation of a prelude of elementary functions.

# Mathematical functions:
def mul(x, y):
    """Multiplies two numbers."""
    return x * y

def id(x):
    """Returns the input unchanged."""
    return x

def add(x, y):
    """Adds two numbers."""
    return x + y

def neg(x):
    """Negates a number."""
    return -x

def lt(x, y):
    """Checks if one number is less than another."""
    return x < y

def eq(x, y):
    """Checks if two numbers are equal."""
    return x == y

def max(x, y):
    """Returns the larger of two numbers."""
    return x if x > y else y

def is_close(x, y):
    """Checks if two numbers are close in value."""
    return abs(x - y) < 1e-2

def sigmoid(x):
    """Calculates the sigmoid function."""
    return 1.0 / (1.0 + math.exp(-x)) if x >= 0 else math.exp(x) / (1.0 + math.exp(x))

def relu(x):
    """Applies the ReLU activation function."""
    return max(0, x)

def log(x):
    """Calculates the natural logarithm."""
    return math.log(x)

def exp(x):
    """Calculates the exponential function."""
    return math.exp(x)

def inv(x):
    """Calculates the reciprocal."""
    return 1.0 / x

def log_back(x, d):
    """Computes the derivative of log times a second argument."""
    return d / x

def inv_back(x, d):
    """Computes the derivative of reciprocal times a second argument."""
    return -d / (x * x)

def relu_back(x, d):
    """Computes the derivative of ReLU times a second argument."""
    return d if x > 0 else 0

# ## Task 0.3 (To be implemented later)
# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

# TODO: Implement for Task 0.3.
