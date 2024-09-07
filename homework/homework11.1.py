sizeofrows=int(input("input size of rows"))
sizeofcols=int(input("input size of columns"))
matrix=[]
transpose=[]
print("input elements of matrix")
for i in range(sizeofrows):
    row=[]
    for j in range(sizeofcols):
        row.append(int(input()))
    matrix.append(row)
for i in range(sizeofcols):
    newrow=[]
    for j in range(sizeofrows):
        newrow.append(matrix[j][i])
    transpose.append(newrow)
print("transpose matrix is")    
for newrow in transpose:
    print(newrow)
