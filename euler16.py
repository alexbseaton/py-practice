# brute force
power = 1000 # expected: 7
result = 0
for digit in str(2 ** power):
    result += int(digit)
print(result)