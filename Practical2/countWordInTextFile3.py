# Count words in a file

file = open("sample.txt", "r")
text = file.read()

words = text.split()
print("Total words:", len(words))

file.close()
