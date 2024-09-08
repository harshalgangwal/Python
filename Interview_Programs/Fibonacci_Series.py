"""n = int(input("enter how many length"))
fib = [0,1]
for i in range(n):
    if n < 1:
        return False
    elif n == 1:
        return

    while n > len(fib):
        fib.append(fib[-1]+fib[-2])
print(fib)"""

def fibonacci(n):
    fib = [0,1]
    if n < 0:
        print("invalid")
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        for i in range(n):
            while len(fib) < n:
                fib.append(fib[-1] + fib[-2])
        return fib

user_input = int(input("length of fibonacci series : "))
print(fibonacci(user_input))