# Problem_Definition:
# Write a Program To REVERSE internal content of every second word present in the given string?

input_string = "India is my country all indians are my brothers"
list1 = input_string.split(" ")
list2 = []
output_string = ''

for i in range(1, len(list1) + 1):
    if i % 2 == 0:
        list2.append(list1[i - 1][::-1])
    else:
        list2.append(list1[i - 1])

print(list2)
output_string = ' '.join(list2)
print(output_string)
