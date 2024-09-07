str="banana"
arr=[]
for i in range(len(str)):
    if(str[i]=="a"):
        arr.append("x")
    else:
        arr.append(str[i])
for i in range(len(arr)):
        print(arr[i],end="")
