make_multiplier=lambda x:lambda y:x*y

multiplier_of_3=make_multiplier(3)
multiplier_of_5=make_multiplier(5)

print(multiplier_of_3(6))
print(multiplier_of_5(6))
print(multiplier_of_3(10))

