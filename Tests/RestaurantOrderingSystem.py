from abc import ABC,abstractmethod


class MenuOperations(ABC):
    @abstractmethod
    def display_menu(self):
        pass
    
    
    @abstractmethod
    def add_dishes(self,dish):
        pass



class dish(ABC):
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    
    @abstractmethod
    def dish_type(self):
        pass    


class appetizer(dish):
    def dish_type(self):
        return "Appetizer"
    

class entrees(dish):
    def dish_type(self):
        return "Entrees"


class Menu(MenuOperations):
    def __init__(self):
        self.dishes=[]
    
    def add_dishes(self, dish):
        self.dishes.append(dish)
   
    def display_menu(self):
        for dish in self.dishes:
            print(dish,dish.price)


class Customer:
    def __init__(self,name,contact_info):
        self.name=name
        self.contact_info=contact_info
        self.order_history=[]
   
   
    def add_order(self,order):
        self.order_history.append(order)
   
   
    def view_order_history(self):
        if self.order_history:
            for order in self.order_history:
                print(order)        
        else:
            print("You havn't done any orders yet")


class Order:
    def __init__(self,customer,dishes):
        self.customer=customer
        self.dishes=dishes
        self.price=sum([dish for dish in dishes])


class Restaurant:
    def __init__(self,name):
        self.name=name
        self.menu=Menu()
        self.customers=[]
    
    def add_customer(self,customer):
        self.customers.append(customer)
    
    
    def find_customer(self,name):
        for customer in self.customers:
            if customer.name==name:
                return customer
            else:
                print("Customer name not found")
    
    
    def place_order(self,customer_name,dish_name):
        customer=self.find_customer(customer_name)
        if customer:
            dishes=[]
            for dish in self.menu.dishes:
                if dish in dish_name:
                    dishes.append(dish)
        else:
            print("Customer not found")
