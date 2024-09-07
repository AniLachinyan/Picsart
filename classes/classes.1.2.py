class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        print(f"Name ->{self.name},Age -> {self.age}")

    def greeting(self):
        print(f"Welcome {self.name}")    

person1=Person("John",99)
person1.details()
person1.greeting()