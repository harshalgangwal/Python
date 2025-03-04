def palindromeNumber(n):
    if n <= 0:
        return "Palindrome is not defined"
    else:
        original = n
        reversedNumber = 0
        while n > 0:
            digit = n % 10
            reversedNumber = reversedNumber * 10 + digit
            n //= 10
        return original == reversedNumber
print(palindromeNumber(12341))