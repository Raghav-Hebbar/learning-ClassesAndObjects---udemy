class Father:
    def FatherProperty(self):
        print("Fathers's property")
    
class Mother:
    def MotherProperty(self):
        print("Mother's property")

class Child( Father, Mother):
    def Property(self):
        print("Child will inherit :")
        super().FatherProperty()
        super().MotherProperty()

c1 = Child()
c1.Property()