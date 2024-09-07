def sum_of_elements(ls):
    if not ls:
        return 0
    return ls[0]+sum_of_elements(ls[1:])
ls=[1,2,3,4,5,6,7]
print(f"sum of digits in {ls} list  is {sum_of_elements(ls)}")
