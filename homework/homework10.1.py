arr=[1,2,3,4,5]
arr1=[1,2,4,4,5]
k=0
if(len(arr)==len(arr1)):
    for i in range(len(arr)):
        if(arr[i]==arr1[i]):
            k+=1

    if(k==len(arr)):
        print("yes")
    else:    
        print("no")
else:
    print("no")
