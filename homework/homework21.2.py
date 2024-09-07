def make_adder(n):
    return lambda x:x+n

adder_of_5=make_adder(5)
adder_of_3=make_adder(3)
adder_of_2=make_adder(2)

print(adder_of_5(3))
print(adder_of_3(10))
print(adder_of_5(6))
print(adder_of_2(4))



