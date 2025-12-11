ls = []
ls.append("Gokul")
ls.append("Sirvi")
ls.insert(0,"kag")
print(ls)
name = ls.pop() 
print(name)
ls.append(1)
ls.remove(1)
print(ls)

ls1 = [1,2,2,1]
print(ls1)
a = len(ls1)-1
print(a)
print(ls1.index(2))
print(ls1)
i=0
c=0
while(i<=a/2):
    if(ls1[i]!=ls1[a-i]):
        c=1
        break
    else:
        c=0
        i=i+1
if(c==0):
    print("Palindrome")
else:
    print("Not Palindrome")
ls1.sort()
print("After Sorting \n",ls1)
