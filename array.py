n = int(input("Enter size: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Array elements:", arr)


arr = [10, 20, 30, 40, 50]

key = int(input("Enter element to search: "))

if key in arr:
    print("Element found.")
else:
    print("Element not found.")



arr = [10, 15, 20, 25, 30]

even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)