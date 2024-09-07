matrix=[]
m=int(input("input size of row "))
n=int(input("input size of column "))
for i in range(m):
    row=[]
    for j in range(n):
        a=int(input())
        row.append(a)
    matrix.append(row)
max=matrix[0][0] 
for i in range(m):
    for j in range(n):
        if(matrix[i][j]>max):
            max=matrix[i][j]
print("maximum number is ",max)            
