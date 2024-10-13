from abc import ABC,abstractmethod
class Person:
    __slots__=["name","age","email"]

    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email


person1=Person("Mary",20,"mary@gmail.com")   
# person1.surname="Smith"->this will raise Error


# ------------------------------------------------------


class MenuItem:
    __slots__=["name","price","ingredients"]

    def __init__(self,name,price,ingredients):
        self.name=name
        self.price=price
        self.ingredients=ingredients


class Appetizer(MenuItem):
    __slots__=["spicy_level"]

    def __init__(self,name,price,ingredients,spicy_level):
        super().__init__(name, price, ingredients)
        self.spicy_level = spicy_level

class Entree(MenuItem):
    __slots__=["cooking"]

    def __init__(self,name,price,ingredients,cooking):
        super().__init__(name, price, ingredients)
        self.cooking=cooking

class Dessert(MenuItem):
    __slots__=["vegan"]

    def __init__(self,name,price,ingredients,vegan):
        super().__init__(name, price, ingredients)
        self.vegan=vegan



class Customer:
    __slots__=["name","contact_info","order_history"]

    def __init__(self,name,contact_info):
        self.name=name
        self.contact_info=contact_info
        self.order_history=[]

    def place_order(self,order):
        self.order_history.append(order)

    def view_order_history(self):
        for history in self.order_history:
            print(history)    

class Order(ABC):
    __slots__ = ['customer', 'menu_items']

    def __init__(self, customer):
        self.customer = customer
        self.menu_items = []

    @abstractmethod
    def calculate_total_price(self):
        pass

class DineInOrder(Order):
    __slots__ = []

    def calculate_total_price(self):
        return sum(item.price for item in self.menu_items)

class TakeawayOrder(Order):
    __slots__ = []

    def calculate_total_price(self):
        return sum(item.price for item in self.menu_items) + 2  

class DeliveryOrder(Order):
    __slots__ = []

    def calculate_total_price(self):
        return sum(item.price for item in self.menu_items) + 5 
    


class Review:
    __slots__ = ['customer_name', 'order', 'rating', 'comments']

    def __init__(self, customer_name, order, rating, comments):
        self.customer_name = customer_name
        self.order = order
        self.rating = rating
        self.comments = comments

        
