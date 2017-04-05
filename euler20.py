from math import factorial
from operator import add
from functools import reduce

def factorial_digit_sum(n):
    num = factorial(n)
    num_as_string = str(num)
    return reduce(add, map(int, num_as_string))

if __name__ == '__main__':
    assert factorial_digit_sum(10) == 27
    print(factorial_digit_sum(100))
