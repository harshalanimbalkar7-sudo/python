numbers = [1, 2, 3, 4, 2, 5, 1, 6]

duplicates = []

for i in numbers:
    if numbers.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)

print("Duplicate elements:", duplicates)



text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)



A = [[1,2,3],
     [4,5,6]]

B = [[7,8,9],
     [1,2,3]]

result = [[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

print(result)


numbers = [45,12,67,23,89]

n = len(numbers)

for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)