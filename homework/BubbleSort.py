ls=[11,31,1,-10,4,23,56]
le=len(ls)
def bubble(ls):
    for i in range(le-1):
        for j in range(le-i-1):
            if (ls[j]>ls[j+1]):
                ls[j],ls[j+1]=ls[j+1],ls[j]

    return ls            


print(bubble(ls))