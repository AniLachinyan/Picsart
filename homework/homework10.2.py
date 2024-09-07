arr=[]
a=0
for i in range(5):
    a=int(input())
    arr.append(a)
maxarr=arr[0]
minarr=arr[0]
for i in range(5):
    if(maxarr<arr[i]):
        maxarr=arr[i]
for i in range(5):
    if(minarr>arr[i]):
        minarr=arr[i]
print(maxarr-minarr)        
