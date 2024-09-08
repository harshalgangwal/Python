# Problem_Definition:
# Write a program to print the characters present at even index and odd index separately for the given string

input_string = "India is my country all indians are my brothers"
even_index_string = ''
odd_index_string = ''

for i in range(0, len(input_string)):
    if i % 2 == 0:
        even_index_string = even_index_string + input_string[i]
    else:
        odd_index_string = odd_index_string + input_string[i]

print("Odd index string : ", odd_index_string)
print("Even index String : ", even_index_string)

# 2nd Approach

input_string = "Harshal Gangwal is a number one coder"
print("Even index Strings : ", input_string[1::2])
print("odd index Strings : ", input_string[::2])
