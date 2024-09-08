Str1 = input("Enter First String: ")
Str2 = input("Enter Second String: ")

#F strings:
print(f"First String is: {Str1}")
print(f"Second String is: {Str2}")

#format Strings using format():
print("First String is: {}".format(Str1))
print("Second String is: {}".format(Str2))

#format number upto two decimal place:
number = 12.789
print(f"Given number is {number:.2f}")
print("Given number is {:.2f}".format(number))