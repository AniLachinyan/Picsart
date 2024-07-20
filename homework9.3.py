ls=[1,2,3]
lastelement=len(ls)-1
newls=[]
for i in range(len(ls)):
    if(ls[i]!=ls[lastelement]):
        newls.append(ls[i])
print(newls)
print(ls[lastelement]," is the last element")

