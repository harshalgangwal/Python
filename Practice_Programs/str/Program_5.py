# Problem_Definition:
# Write a Program To REVERSE internal content of each word

input_string = "India is my country"
output_string = ''
list1 = input_string.split(" ")
list2 = []
print(list1)
for i in list1:
    list2.append(i[::-1])
print(list2)
output_string = ' '.join(list2)
print("Output : ", output_string)