def power_factory(n):

    return lambda x:x**n

power_factory_3=power_factory(3)
print(power_factory_3(4))
