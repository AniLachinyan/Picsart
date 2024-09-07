class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def details(self):
        print(f"Name ->{self.name},Age -> {self.__age}")

    def set_age(self,age):
        if(age>=0):
            self.__age=age
        else:
            raise ValueError("Enter valid age")

    def get_age(self):
        return self.__age   
            

person1=Person("John",22)
person1.details()


print(f"Age is {person1.get_age()}")

person1.set_age(88)
print(f"Updated Age is {person1.get_age()}")