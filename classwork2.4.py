def factorial(n):
    fact=1
    for i in range(n):
        fact*=(i+1)
    return fact

def myfunc(a=None,b=None,c=None,d=None):
    if(b==None and c==None and d==None):
        return factorial(a)
    elif(c==None and d==None):
        return a**b
    elif(d==None):
        return a*b*c
    else:
        return (a+b+c+d)
print(myfunc(5,3))    
    

