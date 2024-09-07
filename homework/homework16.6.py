def len_list(ls):
    if not ls:
        return 0
    return 1+len_list(ls[1:])
ls=[1,2,3,4,5,6]
print(f"Length of list is {len_list(ls)}")
