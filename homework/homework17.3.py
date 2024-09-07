def ascending_order(ls):
    if len(ls)<=1:
        return True
    if(ls[0]>ls[1]):
        return False
    return ascending_order(ls[1:])
ls=[1,2,3,14,5]
print(ascending_order(ls))
