#swapping of values with temp variable:
a = 10
b = 20
temp = a   #Store value of a in temp variable
a = b      #Assigning value of b into a
b = temp   #Assigning value of temp variable i.e. initial value of a into b

print("values of a,b after swapping", a,",",b)


#Swapping of values without temp variable:
h = 30
s = 50
h = h + s    # 30+50 = 80
s = h - s    # 80-50 = 30
h = h - s    # 80-30 = 50

print("values of h,s after swapping", h,",",s)

#Swapping of values without any operations:

p = 20
q = 30
p,q = q,p
print("values of p,q after swapping", p,",",q)