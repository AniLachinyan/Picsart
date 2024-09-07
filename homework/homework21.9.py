def make_accumulator(start=0):

    total=start

    def accumulator(x):
        nonlocal total
        total+=x
        return total
    return accumulator
make_accumulator_0=make_accumulator()
make_accumulator_5=make_accumulator(5)

print(make_accumulator_0(10))
print(make_accumulator_0(20))
print(make_accumulator_0(13))


print(make_accumulator_5(10))
print(make_accumulator_5(20))
print(make_accumulator_5(13))

