# lst = [7, 10, 4, 3, 20, 15]
# l1 = sorted(lst)
# print(l1[-2])
try:
    def kthHighest(k,lst=[]):
        l1 = sorted(lst)
        print(l1[-k])
except IndexError as e:
    print("index out of bound",e)
finally:
    print("Execution successfully")

kthHighest(8,[7, 10, 4, 3, 20, 15])