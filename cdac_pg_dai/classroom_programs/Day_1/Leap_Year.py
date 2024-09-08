Year = int(input("Enter The Year"))

if Year % 4 == 0 and (Year % 100 != 0 or Year % 400 == 0):
    print("{} is a Leap Year".format(Year))
else:
    print("{} is a not a leap year.".format(Year))