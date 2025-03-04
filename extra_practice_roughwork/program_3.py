# x=15
# n=int(input("enter number"))
# for i in range(n):
#           if i==x:
#                 break
# else:
#          print("number not found")
# str1="hi, how are you?"
# print(str1.strip("hi o,?u"))
# print(str1)

# a=20
# b=30
# (a,b)=(b,b)
# print(b,a)

# def testfunct():
#     x=100
#     print(x,end=" ")
# x=10
# testfunct()
# print(x)

# class TestClass:
#     check=[]
#     def __init__(self,a=0,b=0,p=5):
#             self.x=a
#             self.__y=b
#     check.append(p)
# p=TestClass(12,13)

lst=[34,23,11,42,56,43]
lst1=list(filter(lambda x:x%2==0,lst))
print(lst1)