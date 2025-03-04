print("Welcome to python pizza Deliveries!")
size = input("what size pizza do you want? S,M or L:").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N:").lower()
extra_cheese = input("Do you want extra cheese? Y or N:").lower()
total_bill = 0

if size == "s":
    total_bill += 15
    if pepperoni == "y":
        total_bill += 2
elif size == "m":
    total_bill += 20
    if pepperoni == "y":
        total_bill += 3
elif size == "l":
    total_bill += 25
    if pepperoni == "y":
        total_bill += 3

if extra_cheese == "y":
    total_bill += 1

print(f"Total Bill for Your pizza is : ${total_bill}")
