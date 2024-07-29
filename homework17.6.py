def fibonacci(n):
    fib=[]
    a=0
    b=1
    while(n>0):
        fib.append(b)
        b=a+b
        a=b
        n-=1
    return fib    

print(fibonacci(8))        
