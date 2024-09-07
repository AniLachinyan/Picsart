def product_details(name,price,quantity,description):
    print(f"Product name: {name}")
    print(f"Product price: {price}")
    print(f"Product quantity: {quantity}")
    print(f"Product description: {description}")
product={
        'name': 'Macbook pro',
        'price': "2000$",
        'quantity': "10/9",
        'description': "A high-performance laptop with 16GB RAM and 512GB SSD."
        }    
product_details(**product)
