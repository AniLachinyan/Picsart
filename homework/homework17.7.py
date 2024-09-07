def degree_of_2(n):
    if(n<=0):
        return False
    elif(n==1):
        return True
    for i in range(n//2+1):
        if(n==2**i):
            return True
    return False    
n=int(input("Enter your number "))
print(degree_of_2(n))

