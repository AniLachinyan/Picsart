def selection_sort(ls):
    size=len(ls)
    for i in range(size):
        min_index=i
        for j in range(i+1,size):
            if (ls[j]<ls[min_index]):
                min_index=j
        ls[i],ls[min_index]=ls[min_index],ls[i]

    return ls
ls=[12,21,3,4,-3426,45]
print(selection_sort(ls))
