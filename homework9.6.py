ls=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newls=[ls[x] for x in range(len(ls)) if(ls[x]%2==0)]
print(newls)
