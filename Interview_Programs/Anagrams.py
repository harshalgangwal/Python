#validate the input
#convert given string into character array
#sort the both input strings
#check both string equal or not
#if both string are equal then strings are anagrams else not


def is_anagrams(str1, str2):
    if len(str1)!=len(str2):
        return False
    else:
        string1 = str1.lower()
        string2 = str2.lower()

        char_array1 = list(string1)
        char_array2 = list(string2)

        char_array1.sort()
        char_array2.sort()

        # Compare the sorted arrays
        
        if char_array1 == char_array2:
            return "Strings are anagrams"
        else:
            return "Strings are not anagrams"





str1 = "listen"
str2 = "silent"
print(is_anagrams(str1,str2))

