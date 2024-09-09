class Employee:
    def __init__(self,employee_id,name,salary):
        self.__employee_id=employee_id
        self.__name=name
        self.__salary=salary

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self,employee_id):
        self.__employee_id=employee_id

     
    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name

    
    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if(salary>=0):
            self.__salary=salary
        else:
            raise ValueError("Salary can't be negative")

    
    def display_employee_detail(self):
        print(f"Employee ID is {self.__employee_id}, Name is {self.__name}, Salary is {self.__salary}")


employee=Employee(100,"Ann",10000)
employee.display_employee_detail()


employee.set_name("Jon")
employee.set_salary(8000)

employee.display_employee_detail()




