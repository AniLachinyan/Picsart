def mylist(ls):
    if not ls:
        return
    print(ls[0])
    return mylist(ls[1:])
ls=[1,2,3,4,5,6]
mylist(ls)
