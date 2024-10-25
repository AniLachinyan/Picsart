from abc import ABC,abstractmethod


class SalesOperation(ABC):
    @abstractmethod
    def calculate_commision(self,amount):
        pass


class Car(ABC):
    def __init__(self,make,model,price):
        self.make=make
        self.model=model
        self.price=price



    @property
    def price(self):
        return self.price

    @price.setter
    def price(self,price):
        if not isinstance(price,(int,float)):
            raise  ValueError("Please enter valid price")
        elif price<=0:
            raise ValueError("Enter valid price")
        else:
            self.price=price
   
    @abstractmethod
    def car_type(self):
        pass

    def __repr__(self):

        return f"car make is {self.make},model is {self.model},price is {self.price}"

    
class Customers:
    def __init__(self,name,contact_information):
        self.name=name
        self.contact_information=contact_information

    def __repr__(self):
        return f"Customer name is{self.name} and contact information is {self.contact_information}"    

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self,name):
        if isinstance(name,str) and name!="":
            self.name=name
        else:
            raise ValueError("Please enter valid name")
        


class SalesPerson:
    def __init__(self,name,comission_rate):
        self.name=name
        self.comission_rate=comission_rate
        self.sales_history=[]

    def calculate_comission(self,amount):
        return amount*self.comission_rate
    

    def __repr__(self):
        return f"Saler Name is {self.name},comission rate is {self.comission_rate}"
    

class InventoryManagement(ABC):
    @abstractmethod
    def add_car(self,car:Car):
        pass

    @abstractmethod
    def remove_car(self,car:Car):
        pass

    @abstractmethod
    def display(self):
        pass

class CustomerManagement(ABC):

    @abstractmethod
    def search_car(self,make,model):
        pass

    @abstractmethod
    def purchase_car(self,car:Car,customer:Customers,salesperson:SalesPerson):
        pass


class SalesManagement(ABC):

    @abstractmethod
    def view_history(self):
        pass



class Dealership(InventoryManagement,CustomerManagement,SalesManagement):
    def __init__(self):
        self.inventory=[]
        self.customers=[]
        self.salers=[]

        
    def add_car(self,car:Car):
        self.inventory.append(car)

    def remove_car(self, car:Car):
        if car in self.cart:
            self.inventory.remove(car)
        else:
            print("Car is not in cart")

    def display(self):
        return f"This car(s) is/are available-{self.inventory}" 


    def search_car(self, make, model):
        for car in self.cart:
            if car.model==model and car.make==make:
                print("Car found!")
                return car
            print("Car not found")



    def purchase_car(self, car:Car, customer:Customers, salesperson:SalesPerson):
        if car in self.inventory:
            self.remove_car(car)
            purchase_amount=car.price
            commission=salesperson.calculate_comission(purchase_amount)
            salesperson.sales_history.append((car,customer,purchase_amount,commission))
            self.customers.append(customer)
            print(f"Customer {customer.name} purchased {car},the commision is {commission}")
        else:
            print(f"Car is not available...")    


    def view_history(self):
        for salesperson in self.salers:

            if salesperson.sales_history:
                print (f"Salesperson->{salesperson.name}")
                for sale in salesperson.sales_history:
                    car,customer,purchase_amount,commission=sale
                    print(f"Sold {car} to {customer.name} for {purchase_amount},Commission was {commission}")
            else:
                print(f"{salesperson.name} has no sales yet")

                
    def add_salesperson(self,salesperson:SalesPerson):
        self.salers.append(salesperson)
        print(f"New Salesperson is {salesperson.name}")


        
class electric_car(Car):
    def car_type(self):
        return f"Electric Car"
    
class hybrid_car(Car):
    def car_type(self):
        return f"Hybrid Car"    
