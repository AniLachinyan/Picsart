def make_multiplier_of(n):
    def multiplier(x):
        return f"{x}*{n}={x*n}"
    return multiplier
multiplier_of_3=make_multiplier_of(3)
multiplier_of_5=make_multiplier_of(5)

print(multiplier_of_3(6))
print(multiplier_of_5(5))
print(multiplier_of_3(22))
print(multiplier_of_5(15))
print(multiplier_of_3(8))
