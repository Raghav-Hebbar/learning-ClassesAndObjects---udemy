class Name:
    def __init__(self, firstName, middleName, lastName):
        self.FirstName = firstName
        self.MiddleName = middleName
        self.LastName = lastName

class Student:
    def __init__(self, rollNo, sname,course):
        self.RollNo = rollNo 
        self.StudentName= sname
        self.Course = course

student1 = Student(101,Name("Raghaveshwara","Ramesh","Hebbar"),"OOp With Python")
student2 = Student(102,Name("Imandi","Vijaya","Venkatesh"),"OOp With Python")
student3 = Student(103,Name("Banoth","Rahul","Veeru"),"OOp With Python")

students = [student1, student2, student3]

for student in students:
    print("Roll Number: {}\nStudent Name: {} {} {}\nCourse Enrolled : {}\n".format(student.RollNo, 
    student.StudentName.FirstName, 
    student.StudentName.MiddleName, 
    student.StudentName.LastName,
    student.Course))