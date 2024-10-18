from abc import ABC,abstractmethod


#Single Responsibility Principle
# Bad examole
class Person:
    def __init__(self,name,age,street):
        self.name=name
        self.age=age
        self.street=street

    def isadult(self):
        if self.age>18:
            return True
        return False

    def address(self):
        return f"Address is {self.street}"    
    
# Good example

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class AgeService:
    def isadult(self,person:Person):
        if person.age>18:
            return True
        return False
    
class Address:
    def __init__(self,street):
        self.street=street

    def address(self):
        return f"Address is {self.street}"    
           


#Opend/closed principles
# Bad example

class Shape:
    def __init__(self,shape_type):
        self.shape_type=shape_type

    def area(self):
        if (self.shape=="circle"):
            return 3.14*10*10
        elif (self.shape_type=="rectangle"):
            return 10*10


# Good example

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius        

class Rectangle(Shape):
    def __init__(self,hight,width):
        self.hight=hight
        self.width=width

    def area(self):
        return self.width*self.hight



# Liskov Substitution Principle
# Bad example
class Bird:
    def fly(self):
        print("flying")
class Penguin(Bird):
    def fly(self):
        raise ValueError


# Good example
class Bird(ABC):
    @abstractmethod
    def move():
        pass

class Penguin(Bird):
    def move():
        print("swimming")

class Parrot(Bird):
    def move(self):
        print("flying")


# Interface Segregation Principle
# Bad example

class Worker:
    def work(self):
        pass
    
    def eat(self):
        pass

class OfficeWorker(Worker):
    def work(self):
        print("Working in the office")

    def eat(self):
        print("Eating lunch")

class Robot(Worker):
    def work(self):
        print("Always working")

    def eat(self):
        print("Not eating")



# Good example

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class OfficeWorker(Workable,Eatable):
    def work(self):
        print("Working in the office")

    def eat(self):
        print("Eating lunch")   

class Robot(Workable):
    def work(self):
        print("Always working")



# Dependency Inversion Principle
# Bad example

class Keyboard:
    def type(self):
        return "Typing with keyboard"

class Computer:
    def __init__(self):
        self.keyboard=Keyboard

    def input_device(self):
        return self.keyboard.type()



# Good example

class InputDevice(ABC):
    @abstractmethod
    def input(self):
        pass


class Keyboard(InputDevice):
    def input(self):
        return "Typing with keyboard"
        


class Mouse(InputDevice):
    def input(self):
        return "Clicking with mouse"




class Computer:
    def __init__(self,input_device:InputDevice):
        self.input_device=input_device

    def input_device_used(self):
        return self.input_device.input()


