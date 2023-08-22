from ManagerBL import Manager_BL
class Manager_UI:
    
    @staticmethod
    def TakeProductInputFromAdmin():
        name = input("Enter Product Name: ")
        quantity = float(input("Enter Product Quantity: "))
        price = float(input("Enter Product Price: "))
        if name != None and quantity != None and price != None:
            p = Manager_BL(name,quantity,price)
            return p
        else:
            return None
        
    @staticmethod
    def AdminInterface():
        print("1. View Products")
        print("2. Add Products")
        print("3. Delete Product")
        print("4. Change Quantity")
        print("5. Go Back")
        print("-------------------------")
        option = input("Enter Your Option...")
        return option
        