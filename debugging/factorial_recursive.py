#!/usr/bin/python3
import sys

# Recursive factorial calculation function
# This function takes an integer n and returns its factorial using recursion.
def factorial(n):
    # Parameters:
    #   n (int): the integer for which we want to calculate the factorial.
    #
    # Returns:
    #   int: the factorial of n (n!).
    
    if n == 0:  # Base case: the factorial of 0 is 1.
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call to compute n! = n * (n-1)!

# Retrieve the first command-line argument and convert it to an integer.
f = factorial(int(sys.argv[1]))

# Print the result of the factorial calculation.
print(f)

