# defined the function
def secondsmallestInt(lst):
    smallest = float("inf")  # initialize value a infinity
    second_smallest = float("inf")

# iterate through list
    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_smallest if second_smallest != float('inf') else "No second smallest element"

lst = [10,20,30,40,50]
print("second smallest element : ", secondsmallestInt(lst))

