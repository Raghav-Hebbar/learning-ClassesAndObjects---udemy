from abc import ABC, abstractmethod

class Institute:
    def __init__(self):
        print(type(self).__name__,"Details :")

    def CoursesOfferd(self):
        print("Courses offerd: C, C++, java, .NET")
        
    @abstractmethod
    def address(self) : pass

class TechnoAcademy(Institute):
    def CoursesOfferd(self):
        print("Python, Datascience, Xamarin")
        print("Address @ Hyderabad")

class OnlineAcademy(Institute):
    def address(self):
        print("Address @ Bangalore")


#inst = Institute()
ta = TechnoAcademy()
ta.CoursesOfferd()
ta.address()

olt = OnlineAcademy()
olt.CoursesOfferd()
olt.address()



