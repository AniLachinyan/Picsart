def sum_of_digits(n):
    sum=0
    k=0
    while(n!=0):
        k=n%10
        sum+=k
        n=n//10
    return sum
number=int(input("Input number "))
print("Sum of digits is ",sum_of_digits(number))
