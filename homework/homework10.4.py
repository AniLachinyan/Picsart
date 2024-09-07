matrix=[]

size=int(input("input size of matrix "))
for i in range(size):
    row=[]
    for j in range(size):
        a=int(input())
        row.append(a)
    matrix.append(row)    
for i in range(size):
       temp=matrix[i][i]
       matrix[i][i]=matrix[i][size-i-1]
       matrix[i][size-i-1]=temp
print(matrix)

