# Problem_Definition:
# Write a Program To REVERSE content of the given String by using while loop

str1 = 'Harshal'
str2 = ""

length = len(str1) - 1

while length>=0:
    str2 = str2+str1[length]
    length=length-1
print(str2)
