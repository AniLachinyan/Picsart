def get_nth_element(iterable,n):
    iterator=iter(iterable)
    for i in range(n):
        next(iterator)
    return next(iterator)
list=[1,2,3,4,5,6]
n=4
print(get_nth_element(list,n))
