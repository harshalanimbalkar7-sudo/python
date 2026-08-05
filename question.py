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