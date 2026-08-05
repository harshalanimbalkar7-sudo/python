numbers = [1, 2, 3, 4, 2, 5, 1, 6]

duplicates = []

for i in numbers:
    if numbers.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)

print("Duplicate elements:", duplicates)