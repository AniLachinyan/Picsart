def max_of_3(a,b,c):
    max=a
    if(max<b):
        max=b
    elif(max<c):
        max=c
    return max
a=int(input("input first number "))
b=int(input("input second number "))
c=int(input("input third number "))
print(f"Maximum number is {max_of_3(a,b,c)}")

