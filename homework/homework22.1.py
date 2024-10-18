def fibonacci_generator(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b

for num in fibonacci_generator(10):
    print(num,end=", ")
