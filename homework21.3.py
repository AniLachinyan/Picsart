def apply_twice(f,n):
    return f(f(n))

def square(x):
    return x*x

result=apply_twice(square,3)
print(result)
