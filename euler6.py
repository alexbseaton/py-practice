from functools import reduce
from operator import add, pow

def sum_of_squares(N):
    return (N * (N + 1) * (2*N + 1)) / 6

def square_of_sum(max):
    return ((1 / 2) * max * (max + 1)) ** 2

print(square_of_sum(100) - sum_of_squares(100))