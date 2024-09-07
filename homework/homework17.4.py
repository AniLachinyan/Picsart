def is_prime(n):
    for i in range(2,n//2+1):
        if((n%i)==0):
            return False
    return True
num= int(input("Enter number "))
if(is_prime(num)):
    print(f"Yes {num} is prime number")
else:
    print(f"No {num} is not prime number")
