import csv

# Calculate average of a column

column_index = int(input("Enter column index (0,1,2...): "))

file = open("data.csv", "r")
reader = csv.reader(file)

total = 0
count = 0

for row in reader:
    try:
        value = float(row[column_index])
        total += value
        count += 1
    except:
        pass

if count > 0:
    print("Average:", total / count)
else:
    print("No valid data")

file.close()
