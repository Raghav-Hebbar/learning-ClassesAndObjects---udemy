class GrandParents:
    def PropertyLand(self):
        print("Property Land farming given by GrandParents")

class Parents(GrandParents):
    def PropertyHome(self):
        print("Property Home constructed By parents")

class child(Parents):
    def PropertyVehicle(self):
        print("Property Car Purchased By Child")

    def PropertyLand(self):
        print("Property land of GP is now used for commertial")

c1 = child()
c1.PropertyLand()
c1.PropertyHome()
c1.PropertyVehicle()