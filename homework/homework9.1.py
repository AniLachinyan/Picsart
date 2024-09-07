ls=[1,2,3,4]
newls=[]
count=0
number=int(input("Input number "))
index=int(input("Input index "))
if(index>len(ls)):
    print("input valid index")
else:
    for i in range(len(ls)):
        if(index==i):
            newls.append(number)
            break
        else:
            newls.append(ls[i])
            count+=1
    for i in range(len(ls)-count):
        newls.append(ls[count])
        count+=1
    print(newls)    


