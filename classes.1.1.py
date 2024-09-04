class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        print(f"Name ->{self.name},Age -> {self.age}")

person1=Person("John",99)
person1.details()

