def infinite_sequence():
    num=1
    while True:
        yield num
        num+=1
gen=infinite_sequence()

for i in range(10):
    print(next(gen))
