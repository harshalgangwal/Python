# Problem_Definition:
# Program to sort characters of the string, first alphabet symbols followed by digits

A = "harshu1110Gangwal2001"
B = A.lower()
list1 = []
list2 = []
for i in B:
    if i.isdigit():
        list1.append(i)
    else:
        list2.append(i)
list1.sort()
list2.sort()
list2.extend(list1)
print(list2)


