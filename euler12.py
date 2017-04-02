from math import sqrt
from math import ceil

def n_factors(num):
    assert num >= 1
    result = 0
    for i in range(1, ceil(sqrt(num)) + 1):
        if num % i == 0:
            result += 1
            if i * i != num:
                result += 1
    return result

assert n_factors(1) == 1
assert n_factors(3) == 2
assert n_factors(28) == 6

def tri_num(n):
    return int(n * (n + 1) / 2)

assert tri_num(7) == 28

n = 1
while (n_factors(tri_num(n))) <= 500:
    n += 1

assert n_factors(tri_num(n)) > 500
assert n_factors(tri_num(n-1)) <= 500

print(tri_num(n))