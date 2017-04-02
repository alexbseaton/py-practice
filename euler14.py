# Longest Collatz Sequence
def next_term(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1
# brute force?
max_start = 10 ** 6
max_length = 0
result = 1
for start in range(2, max_start + 1):
    length = 1
    next = start
    while next != 1:
        next = next_term(next)
        length += 1
    if length > max_length:
        max_length = length
        result = start

print(result)
