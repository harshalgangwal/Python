def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(6))


#Approach second

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print(factorial(6))