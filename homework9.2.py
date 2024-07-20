ls=[1,2,3,2,4]
index=int(input())
number=int(input())
newls=[]
count=0
for i in range(len(ls)):
    count=count+1
    if(i==index):
        newls.append(number)
        break
    else:
        newls.append(ls[i])
for i in range(len(ls)-count):
    newls.append(ls[count])
    count=count+1
print(newls)    

