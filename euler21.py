# d(n) means sum of divisors of n that are less than n
# amicable numbers a, b are s.th d(a) = b, d(b) = a and a != b
from operator import add
from functools import reduce

def factors(n):
    the_set = set(reduce(add, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    the_set.remove(n)
    return the_set

def d(n):
    return reduce(add, factors(n))

def main(n):
    result = 0
    for a in range(2, n + 1):
        b = d(a)
        if b == 1 or b > n or a == b:
            continue
        if a == d(b):
            print(a, b)
            result += a + b
    return result // 2
    
if __name__ == '__main__':
    print(main(10000))