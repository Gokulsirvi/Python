# Convert number from one base to another

num = input("Enter number: ")
base_from = int(input("Enter base of number (2-10): "))
base_to = int(input("Enter base to convert (2-10): "))

# Convert to decimal first
decimal = int(num, base_from)

# Convert decimal to new base
result = ""
while decimal > 0:
    remainder = decimal % base_to
    result = str(remainder) + result
    decimal //= base_to

print("Converted number:", result)
