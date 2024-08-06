def make_memorize(f):

    cache={}

    def memorized_function(*args):
        if args in cache:
            return cache[args]
        result=f(*args)
        cache[args]=result
        return result
    return memorized_function


def square(x):
    return x*x
memorized_square=make_memorize(square)

print(memorized_square(10))
print(memorized_square(20))
print(memorized_square(10))

