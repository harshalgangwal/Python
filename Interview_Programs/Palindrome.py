# First Approach
def is_palindrome(s):
    s = s.lower().replace(" ","")
    return s==s[::-1]

print(is_palindrome("eye"))

# Second Approach
def palindrome(s):
    for i in range(0, len(s)//2):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True

print(palindrome("eye"))