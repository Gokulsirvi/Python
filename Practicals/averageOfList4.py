# Calculate average

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

total = 0
for num in numbers:
    total += num

average = total / len(numbers)

print("Average:", average)
