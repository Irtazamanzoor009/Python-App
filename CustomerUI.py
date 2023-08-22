from CustomerBL import Customer_BL
from ProductsDL import Products_DL
from MainMenu import Menu as s
class Customer_UI:
    
    @staticmethod
    def CustomerProductInput(customername):
        name = input("Enter Product Name: ")
        checkProduct = Products_DL.CheckProduct(name)
        if checkProduct == True:
            quantity = float(input("Enter Product Quantity: "))
            price = Products_DL.GetProductPrice(name)
            individualPrice = quantity * float(price)
            if name != None and quantity != None and quantity > 0:
                c = Customer_BL(customername, name , quantity , individualPrice)
                return c
            else:
                return None
        else:
            print("Error! Product Not Found")
            s.Getch()
            return None
        
    @staticmethod
    def CustomerInterface():
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Delete Product")
        print("5. Change Quantity")
        print("6. Clear Cart")
        print("7. Calculate Bill")
        print("8. Go Back")
        print("--------------------------------")
        option = input("Select your option...")
        return option