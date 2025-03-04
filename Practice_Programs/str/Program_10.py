# Problem_Definition:
# Program for the requirement,input: a4b3c2 and expected output: aaaabbbcc

# input_string = "a4b3c2"
# list1 = []
# dict1 = {}
# for i in input_string:
#     list1.append(i)
# print(list1)
# dict1 = dict(list1)
# print(dict1)

def expand_string(s):
    result = ""
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        num = ""
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        result += char * int(num)
    return result

input_str = "a4b3c2"
output_str = expand_string(input_str)
print(output_str)


