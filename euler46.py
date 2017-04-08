""" What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square? """
from math import floor

def primes_up_to(n):
    """ Erastothenes """
    primes = [True]*n
    primes[0] = False
    for i in range(n):
        if not primes[i]:
            continue
        next = 2 * (i + 1)
        while next <= n:
            primes[next - 1] = False
            next += (i + 1)
    return [x + 1 for x in range(n) if primes[x]]

def meets_criterion(n, long, short):
    """ true if there are elements a in long and b in short s.th a + b = n """
    for b in short:
        if n - b in long:
            return True
    return False

def main(upper_limit):
    """ Make lists of primes and squares then chomp through to find a counter-example"""
    primes = primes_up_to(upper_limit)
    twice_squares = [2 * x ** 2 for x in range(1, floor(upper_limit ** 0.5))]
    for odd in [x for x in range(3, upper_limit + 1, 2) if x not in primes]:
        if not meets_criterion(odd, primes, twice_squares):
            return odd
    return -1

if __name__ == '__main__':
    upper_limit = 6000
    print(main(upper_limit))
