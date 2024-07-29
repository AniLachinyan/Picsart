def total_price(*prices,tax_rate=0.1):
    total_price=sum(prices)
    total_price_with_tax=total_price*(1+tax_rate)
    return total_price_with_tax
print(total_price(100,300,500,600))
print(total_price(100,300,500,600,tax_rate=0.9))

