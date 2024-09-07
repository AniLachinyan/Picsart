matrix=[]
sum=0
size=int(input("input size of matrix "))
for i in range(size):
    row=[]
    for j in range(size):
        a=int(input())
        row.append(a)
    matrix.append(row)
for i in range(size):
    for j in range(size):
        if(i==size-j-1):
            sum+=matrix[i][size-i-1]
print("sum is ",sum)            

