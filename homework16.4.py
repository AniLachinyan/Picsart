def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)
n=int(input("input number "))
result=sum(n)
print(f"Sum from 1 to {n} is {result}")
