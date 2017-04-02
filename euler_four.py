# Palindromic numbers

def is_palindrome(n):
    return str(n) == str(n)[::-1]

big_palindrome = 1
for left in range(1, 999):
    for right in range(left, 999):
        if is_palindrome(left * right) and left * right > big_palindrome:
            big_palindrome = left * right
print(big_palindrome)