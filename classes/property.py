#1------------------------------------------------------------------------------
class Person:
    def __init__(self, name: str, age: int ):
        self.__name=name
        self.__age=age

    @property
    def age(self):
        return self.__age    
    

    @age.setter
    def age(self,new_age):
        if (isinstance(new_age,int) and new_age>0):
            self.__age=new_age
        else:
            raise ValueError("Please enter valid age")


#2-------------------------------------------------------------------------------

class Rectangle:
    def __init__(self,width: float, height: float):
        self.__width=width
        self.__height=height


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,new_width):
        if new_width<=0:
            raise ValueError("Rectangle must have positive width")
        else:self.__width=new_width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,new_height):
        if new_height<=0:
            raise ValueError("Rectangle must have positive height")
        else:
            self.__height=new_height
    @property
    def area(self):
        return self.__height*self.__width

    @property
    def perimeter(self):
        return 2*(self.__width+self.__height)    
    
#3-----------------------------------------------------------------------------



class Temperature:
    def __init__(self,celsius):
        self.__celsius=celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError
        else:
            self.__celsius=value   


    @property 
    def fahrenheit(self):
        return (self.__celsius*(9/5))+32
    
    @fahrenheit.setter
    def fahrenheit(self,value):
        self.__celsius=(value-32)*(5/9)

#4----------------------------------------------------------------------------
class Descriptor:
    def __get__(self,instance,owner):
        return instance._score
    
    def __set__(self,instance,value):
        if not (value>=0 and value<=100):
            raise ValueError("Score must be more than 0 and less than 100")
        else:
            instance._score=value

class Student:
    score=Descriptor()

    def __init__(self,name,score):
        self.name=name
        self.score=score



#5----------------------------------------------------------------------------


class ValidatedString:
    def __init__(self,length):
        self.length=length

    def __get__(self,instance,owner):
        return instance.__name
    

    def __set__(self,instance,value):
        if not isinstance(value,str):
            raise ValueError("Enter valid name")
        if len(value)<self.length:
            raise ValueError(f"Length of name must be at least {value}")
        instance.__name=value

class User:
    name=ValidatedString(5)
    def __init__(self,name,):
        self.name=name

# 6----------------------------------------------------------------------

class Salary:
    def __init__(self,max_salary):
        self.max_salary=max_salary


    def __get__(self,instance,owner):
        return instance.__salary 
    

    def __set__(self,instance,value):
        if not isinstance(value,(int,float)):
            raise ValueError("Please enter valid salary")
        if value>self.max_salary:
            raise ValueError(f"Salary cannot exceed {self.max_salary}.")
        if value<=0:
            raise ValueError("Salary must be positive")
        instance.__salary=value


class Employee:
    salary=Salary(150000)   

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

# 7------------------------------------------------------------------------

class Descriptor():
    def __init__(self,min_value,max_value):
        self.min_value=min_value
        self.max_value=max_value

    def __get__(self,instance,owner):
        return instance.__price

    def __set__(self,instance,value):
        if not isinstance(value,(int,float)):
            raise ValueError("The price must be a number.")
        if value<self.min_value or value>self.max_value:
            raise ValueError(f"Price must be between {self.min_value} and {self.max_value}")
        instance.__price=value



class Product:
    price=Descriptor(1,100)

    def __init__(self,price):
        self.price=price

# 8-------------------------------------------------------------------------
class PasswordValidator:
    def __init__(self,min_length):
        self.min_length=min_length

    def __get__(self,instance,owner):
        return instance.__password

    def __set__(self,instance,value):
        if not isinstance(value,str):
            raise ValueError("Password is not valid")
        if len(value)<self.min_length:
            raise ValueError(f"Password must be at least {self.min_length}.")
        instance.__password=value

class Account:

    password=PasswordValidator(min_length=8)

    def __init__(self,username,password):
        self.username=username
        self.password=password

