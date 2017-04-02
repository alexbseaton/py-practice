# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?
from functools import *
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(max):
    """Return lcm of args."""   
    return reduce(lcm, range(1, max + 1))

print(lcmm(20))