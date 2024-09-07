def manually_iterates(numbers):
    iterator=iter(numbers)

    while True:
        number=next(iterator, None)
        if number is None:
            break
        print(number)

numbers=[1,2,3,4,5]
manually_iterates(numbers)

