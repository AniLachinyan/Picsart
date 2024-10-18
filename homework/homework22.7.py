def custom_range(start,end,step):
    current=start
    while current<end:
        yield current
        current+=step

for num in custom_range(0,5,0.5):
    print(num)
