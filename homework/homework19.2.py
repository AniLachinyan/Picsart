def my_filter(predicate, iterable):
    result=[]
    for item in iterable:
        if(predicate(item)):
            result.append(item)
    return result
def is_even(n):
    return n%2==0
num=[1,2,3,4,5,6,7,8]
print(f"Even numbers: {my_filter(is_even,num)}")
