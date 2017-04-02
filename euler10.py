# Find sum of all primes below two million
max = 2 * 10 ** 6
arr = [True]*max
arr[0] = False

for i in range(max):
    if arr[i]:
        next = 2 * (i + 1)
        while next <= max:
            arr[next - 1] = False
            next += (i + 1)

result = 0
for index, val in enumerate(arr):
    if val:
        result += (index + 1)

print(result)