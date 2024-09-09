class ShoppingCart:
    def __init__(self):
        self.__items=[]

    def add_items(self,name,price):
        if price<0:
            raise ValueError("Price can't be negative")
        self.__items.append({"name":name,"price":price})

    
    def remove_item(self,name):
        for item in self.__items:
            if item["name"]==name:
                self.__items.remove(item)
                return

        raise ValueError(f"Item '{name}' not found in cart")

    def total_items(self):

        return len(self.items)


    def display_cart(self):
        if not self.__items:
            print("Shopping cart is empty")
        else:
            print("Items in the shopping cart-> ")
            for item in self.__items:
                print(f"{item['name']} is {item['price']}$")


cart = ShoppingCart()
cart.add_items("Apple", 1.5)
cart.add_items("Banana", 0.75)
cart.add_items("Orange", 1.25)


cart.display_cart()

cart.remove_item("Banana")

cart.display_cart()                
