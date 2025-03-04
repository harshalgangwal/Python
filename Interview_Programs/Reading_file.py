# #
# # # a = 5
# # # b = 0
# # # print(a//b)
# # # print(type(a//b))
# #
# # a = 7
# # b = 3
# # print(a & b)
# lst = ['cat','dog','elephant','rabbit','goat','lion']
# for i in range(10):
#     lst1 = []
#     for j in lst:
#         if len(j) == i:
#             lst1.append(j)
#     if len(lst1) == 0:
#         pass
#     else:
#         print(i,"letter string :",len(lst1),":",lst1)

def highest_odd_number(num):
    # Convert the number to a string for processing
    num_str = str(num)

    # Extract all digits from the number that are odd
    odd_digits = [digit for digit in num_str if int(digit) % 2 != 0]

    # If no odd digits are found, return 0
    if not odd_digits:
        return 0

    # Construct the highest odd number using the odd digits
    highest_odd = int(''.join(odd_digits))
    return highest_odd


# Examples
input1 = 544286
input2 = 63612248
input3 = 636194581

print(highest_odd_number(input1))  # Output: 5
print(highest_odd_number(input2))  # Output: 6361
print(highest_odd_number(input3))