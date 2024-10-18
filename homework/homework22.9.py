def gen1():
    for i in range(1,6):
        yield i

def gen2():
    yield from gen1()
    for j in range(6,11):
        yield j

for i in gen2():
    print(i)

