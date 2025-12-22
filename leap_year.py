n = int(input("Enter year you want to check : "))
if(n%4==0 and n%100 != 0) or(n%400 == 0):
    print("Leap year ")
else:
    print("Not a Leap Year ")
