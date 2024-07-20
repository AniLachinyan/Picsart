arr=[]
size=int(input("enter size of matrix"))
for i in range(size):
    for j in range(size):
        a=int(input())
        arr.append(a)
for i in range(size):
    for j in range(size):
        print(arr[j],end=", ")
