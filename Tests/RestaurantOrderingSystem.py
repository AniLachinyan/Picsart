from abc import ABC,abstractmethod

class course_assignment(ABC):
    def __init__(self,title,maxscore):
        self.title=title
        self.maxscore=maxscore
        self.submissions={}

    @abstractmethod
    def submit_assignment(self,student,score):
        pass



class Course(ABC):
    def __init__(self,name,instructor):
        self.name=name
        self.instructor=instructor
        self.students=[]
        self.assignments=[]


    def add_students(self,student):
        if student not in self.students:
            self.students.append(student)
        else:
            print("Student is already enrolled")


    def add_assignment(self,assignment):
        if assignment not in self.assignments:
            self.assignments.append(assignment)
        else:
            print("You already have this assignment")

    def view_students(self):
        for student in self.students:
            print(student.name)                    


class UndergraduatedCourse(Course):
    def __init__(self, name, instructor):
        super().__init__(name, instructor)


class GraduatedCourse(Course):
    def __init__(self, name, instructor):
        super().__init__(name, instructor)



class CourseAssignment(course_assignment):
    def CheckAssignment(self,student,score):
        if score<self.maxscore:
            self.submissions[student.name]=score
            student.complited_assignment[self.title]=score
        else:
            print(f"Score must be less than {self.maxscore}")



class Profesor:
    def __init__(self,name,contact_info):
        self.name=name
        self.contact_info=contact_info
        self.courses=[]


    def creat_course(self,course_type,course_name):
        if (course_type=="Undergraduated"):
            course=UndergraduatedCourse(course_name,self)
        elif (course_type=="Graduated"):
            course=UndergraduatedCourse(course_name,self)
        else:
            print("Invalid cource!")    
        
        self.courses.append(course)
        return course
    
    def view_course(self):
        for course in self.courses:
            print(course.name)


class Student:
    def __init__(self,name,contact_info):
        self.name=name
        self.contact_info=contact_info
        self.courses=[]
        self.complited_assignments=[]


    def enroll(self,course:Course):
        course.add_students(self)


    def view_progress(self):
        for assignment in self.complited_assignments:
            print(assignment)