str="reverse me"
arr=[]
i=len(str)
while(i!=0):
    arr.append(str[i-1])
    i=i-1
for k in range(len(arr)):
    print(arr[k],end="")

