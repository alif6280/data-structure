def bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

numbers = [5,3,8,2,1,9,4,6,10,7]
print("Before sorting:", *numbers)
bubble_sort(numbers)
print("After sorting: ", *numbers)
