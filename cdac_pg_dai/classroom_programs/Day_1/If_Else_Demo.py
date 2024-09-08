Total_Amount = 0
Persons = int(input("Enter the number of Persons: "))
for i in range(1,Persons+1):
    Age = int(input("Enter the age of a person {}: ".format(i)))
    if Age < 5:
        print("Ticket is Free!!!")
    elif Age <= 12:
        print("Price of Ticket is 5 RS.")
        Total_Amount += 5
    elif Age <= 60:
        print("Price of Ticket is 10 RS.")
        Total_Amount += 10
    else:
        print("Price of Ticket is 7 RS.")
        Total_Amount += 7

print("Total {} persons ticket amount is RS {}".format(Persons,Total_Amount))
