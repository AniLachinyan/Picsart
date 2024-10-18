def exception_propagator(iterable):
    for item in iterable:
        if item=="error":
            raise ValueError("An error occured!!!")
        yield item

for item in exception_propagator([1,2,"error",3,4]):
    print(item)
