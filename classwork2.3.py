def myfunc(a,b,c):
    if(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return  (int(a)*int(b)*int(c))
    elif(isinstance(a,str) and isinstance(b,int) and isinstance(c,int)):
        return (a*b**c)
    elif(isinstance(a,str) and isinstance(b,str) and isinstance(c,str)):
        return (a+b+c)
    else:
        return None
a=5
b=1
c=3
print(myfunc(a,b,c))  

