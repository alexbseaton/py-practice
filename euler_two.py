from functools import reduce
from operator import add
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return fib(n-1) + fib(n-2) 


limit = 4 * 10 ** 6
#limit = 8

n = 0
while fib(n) < limit:
    n += 1

print(reduce(add, [fib(x) for x in range(1, n+1) if fib(x) % 2 == 0 and fib(x) < limit + 1]))
