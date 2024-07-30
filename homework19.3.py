def my_zip(*iterables):
    min_length=min(len(iterable) for iterable in iterables)
    result=[]
    for i in range(min_length):
        tuple_element=tuple(iterable[i] for iterable in iterables)
        result.append(tuple_element)
    return result
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
symbols = ['!', '@', '#']
print(my_zip(numbers, letters, symbols))
