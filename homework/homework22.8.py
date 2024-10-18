def even_numbers(numbers):
    return (num for num in numbers if num%2==0)

for even in even_numbers(list(range(1,51))):
    print(even)


