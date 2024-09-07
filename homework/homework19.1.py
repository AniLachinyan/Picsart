def my_map(func,iterable):
    result=[]
    for item in iterable:
        result.append(func(item))
    return result

def square(x):
    return x*x

result=my_map(square,[1,2,3,4,5,6])
print(result)
