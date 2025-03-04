# String1 = "Harshal"
# Rev_str = String1[::-1]
# print(Rev_str)


# Ls = [1,2,3,4]
# sum = 0
# for i in Ls:
#     sum += i
# print(sum)

str1 = "silent"
str2 = "listen"

def anagrams(s1,s2):
    if len(s1) != len(s2):
        return "strings not an anagrams"
    elif len(s1) == len(s2):
        s1 = sorted(s1)
        s2 = sorted(s2)
        if s1 == s2:
            return "Strings are Anagrams"
        else:
            return "strings are not anagrams"

print(anagrams("listen","silent"))
