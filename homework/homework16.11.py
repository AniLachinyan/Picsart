def sum_of_digits(n):
    if (n<10):
        return n
    return n%10+sum_of_digits(n//10)
num=int(input("Enter number "))
print(f"Sum of digits {num} is {sum_of_digits(num)}")