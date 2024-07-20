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
        if(i==j):
            sum+=matrix[i][j]
print("sum is  ",sum)            
