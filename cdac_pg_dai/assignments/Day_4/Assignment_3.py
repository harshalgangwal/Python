list1 = []
for i in range(1, 21):
    list1.append(i)
# print(list1)
Siya = ["FizzBuzz" if x % 3 == 0 and x % 5 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else x for x in list1]
print(Siya)
