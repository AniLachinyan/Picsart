str="radar"
arr=[]
i=len(str)
arr1=[]
answer=True
for n in range(len(str)):
    arr1.append(str[n])
while(i!=0):
    arr.append(str[i-1])
    i=i-1
for c in range(len(arr)):
    if(arr[c]!=arr1[c]):
        answer=False
        break    
    else:
        continue
if(answer==True):
    print("yes it's palindrom")
else:
    print("no it's not palindrom")

