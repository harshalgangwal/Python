try:
    x = 10/2
except ZeroDivisionError as e:
    print("Cannot divide by zero :",e)
finally:
    print("Execution is completed")
