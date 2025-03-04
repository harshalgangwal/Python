lst1 = [1,2,3,4]
lst2 = [3,4,5,6]

for i in lst2:
    lst1.append(i)

print(set(lst1))

lst1.extend(lst2)   # Modifies lst1 in place
print(lst1)