#str=“hello, world! are you ready?”
#newstr=str.title()
#print(newstr)
str="hello, world! are you ready?"
arr=[]
for i in range(len(str)):
    arr.append(str[i])
for i in range(len(arr)):
    if(arr[i]==" "):
        arr[i+1]=chr(ord(arr[i+1])-32)
arr[0]=chr(ord(arr[0])-32)
for i in range(len(arr)):
    print(arr[i],end="")

