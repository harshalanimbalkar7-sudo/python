# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not Prime")

   
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact

# num = int(input("Enter number: "))
# print("Factorial =", factorial(num))  

# text = input("Enter a string: ")

# count = 0

# for ch in text.lower():
#     if ch in "aeiou":
#         count += 1

# print("Total vowels:", count)


# numbers = list(map(int, input("Enter numbers: ").split()))

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print("Largest =", largest)


arr = list(map(int, input("Enter numbers: ").split()))

n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)