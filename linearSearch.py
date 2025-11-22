import random

n = int(input("Enter number of array: "))

arr = [random.randint(0, 99) for _ in range(n)]

print("Random numbers are:")
print(*arr)

item = int(input("Enter item to search: "))

com = 0
for i in range(n):
    com += 1
    if arr[i] == item:
        print(f"Item found at {i+1} position and total compare {com}")
        break
else:
    print("Item not found")
