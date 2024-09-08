# Problem_Definition:
# Write a program to merge characters of 2 strings into a single string by taking characters alternatively

first_string = "first string"
second_string = "second string"
output_string = ''
i = 0
j = 0

while i < len(first_string) or j < len(second_string):
    if i < len(first_string):
        output_string = output_string + first_string[i]
        i += 1
    if j < len(second_string):
        output_string = output_string + second_string[j]
        j += 1
print(output_string)
