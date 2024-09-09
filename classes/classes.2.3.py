class Student:
    def __init__(self,name,roll_number,grades):
        self.__name=name
        self.__roll_number=roll_number
        self.__grades=grades

    def set_name(self,name):
        self__name=name

    def get_name(self):
        return self.__name


    def set_roll_number(self,roll_number):
        self.__roll_number=roll_number

    def get_roll_number(self):
        return self.__roll_number


    def set_grades(self,grades):
        if(grades<100 and grades>0):
            self.__grades=grades
        else:
            raise ValueError("Grade must be between 0 and 100")

    def get_grades(self):
        return self.__grades

    def students_detail(self):
        print(f"Student's name is {self.__name}, roll number is {self.__roll_number}, grade is {self.__grades}")


student1=Student("Jon",55,96)
student1.students_detail()

student1.set_grades(-99)
student1.students_detail()


