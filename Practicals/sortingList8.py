# Sort list

numbers = list(map(int, input("Enter numbers: ").split()))

choice = input("Enter 'A' for ascending or 'D' for descending: ")

if choice == 'A':
    numbers.sort()
elif choice == 'D':
    numbers.sort(reverse=True)

print("Sorted list:", numbers)
