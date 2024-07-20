size=int(input("input size of matrix "))
matrix=[]
rotatedmatrix=[]
print("input elements of matrix ")
for i in range(size):
    row=[]
    for j in range(size):
        row.append(int(input()))
    matrix.append(row)
for i in range(size-1,-1,-1):
    newrow=[]
    for j in range(size-1,-1,-1):
        newrow.append(matrix[i][j])
    rotatedmatrix.append(newrow)
print("rotated matrix is ")    
for newrow in rotatedmatrix:
    print(newrow)
