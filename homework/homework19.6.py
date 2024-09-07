def apply_function(iterable,func):
    return [func(element) for element in iterable]
def square(x):
    return x*x
num=[1,2,3,4,5]
print(apply_function(num,square))
