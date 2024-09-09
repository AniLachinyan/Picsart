class Product:
    def __init__(self, product_id, product_name, quantity_in_stock):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__quantity_in_stock = quantity_in_stock

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_quantity_in_stock(self):
        return self.__quantity_in_stock

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_quantity_in_stock(self, quantity):
        if quantity >= 0:
            self.__quantity_in_stock = quantity
        else:
            raise ValueError("Quantity cannot be negative")



    def add_stock(self, quantity):
        if quantity > 0:
            self.__quantity_in_stock += quantity
        else:
            raise ValueError("Cannot add negative or zero")

    def reduce_stock(self, quantity):
        if quantity > 0:
            if self.__quantity_in_stock >= quantity:
                self.__quantity_in_stock -= quantity
            else:
                raise ValueError("Not enough stock to reduce")
        else:
            raise ValueError("Reduction quantity must be positive")


    def display_product_details(self):
        print(f"Product ID is {self.__product_id}, Name is {self.__product_name}, Stock is {self.__quantity_in_stock}")


product = Product(101, "Laptop", 50)


product.display_product_details()


product.add_stock(20)


product.reduce_stock(10)


product.display_product_details()
