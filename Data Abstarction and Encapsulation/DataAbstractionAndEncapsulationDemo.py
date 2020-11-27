class Product:

    def __init__(self):
        self.__productId = ""
        self.__ProductName = ""
        self.__price = ""

    def SetProduct(self, pid, pname,price):
        self.__productId = pid
        self.__ProductName = pname
        self.__price = price

    def ShowProduct(self):
        print("Product ID : {}\nProduct Name : {}\nPrice : {}".format(self.__productId, self.__ProductName, self.__price)) 
    
    def updateProduct(self,newPrice):
        self.__price = newPrice
    
tv = Product()
tv.SetProduct("TV101","LG Gloden Eye", 18500)
tv.ShowProduct()