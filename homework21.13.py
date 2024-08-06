def bar(n):

    functions=[]

    for i in range(n):
        def make_multiplier(index):
            def multiplier(x):
                return x*index
            return multiplier
        functions.append(make_multiplier(i))


    return functions

func_list=bar(3)

for index,func in enumerate(func_list):
    print(f"Function {index} result for 10: {func(10)}")
    print(f"Function {index} __closure__: {func.__closure__}")
    if func.__closure__:
        print(func.__closure__[0].cell_contents)


