def compound_interest(principal, rate, times, years):
    return principal * (1 + rate / times) ** (times * years)
def investment_return(principal, rate, years):
    return principal * (1 + rate * years)
dict={

        "compound":compound_interest,
        "investment":investment_return
        }
def financial_calculator(operation,**kwargs):
    if operation in dict:
        return dict[operation](**kwargs)
    else:
        raise ValueError(f"Unsupported financial operation {operation}")


print(financial_calculator("compound", principal=1000, rate=0.05, times=4, years=1))
print(financial_calculator("investment", principal=1000, rate=0.05, years=10))

