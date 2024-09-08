#integer Type

a = 10
b = 20
c = a+b      #Arithmetic Operator
print("Sum of Two Numbers: ", c)

#String Type

a = "Harshal"
b = "Gangwal"
c = a[:5]    #Slicing Operator
print(c)
print("Sum of Two Numbers: ", a + b)

#Float Type

a = 5.7
b = 6.8
c = a * b
print("product of two numbers: ", c)

d = int(c)   #Type Casting - Explicit
print("Type casting from float to int", d)

#Boolean Type
a = 10
b = 20
c = b/a     #Type casting - Implicit
print("Division of two number is: ",c)

d = b > a
print(d)   #Boolean Type