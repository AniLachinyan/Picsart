def factorial(n):
    fact=1
    for i in range(n):
        fact*=(i+1)
    return fact
number=int(input("Input number "))
print(f"factorial of {number} is ",factorial(number))
