from MainMenu import Menu as s
from MUserDL import MUser_DL
from SignUpUI import SignUp_UI as SignUpUI
from SignInUI import SignIn_UI as SignInUI
from ManagerUI import Manager_UI as AdminUI
from ProductsDL import Products_DL
from CustomerUI import Customer_UI as CustUI
from CustomerCartDL import CustomerCart_DL

def main():
    userpath = "Users.txt"
    productpath = "Products.txt"
    customercart = "customercart.txt"
    s.ClearScreen()
    MUser_DL.ReadUserFromFile(userpath)
    Products_DL.ReadProductFromFile(productpath)
    CustomerCart_DL.ReadCustomerCart(customercart)
    option = None
    while option != "4":
        s.ClearScreen()
        option = s.MenuLogin()
        if option == "1": # sign in
            user = SignInUI.TakeInputWithoutRole()
            if user != None:
                check = MUser_DL.CheckUser(user)
                if check == True:
                    getrole = MUser_DL.GetRole(user)
                    if(getrole == "Admin" or getrole == "admin"):
                        s.ClearScreen()
                        Adminop = None
                        while Adminop != "5":
                            s.ClearScreen()
                            Adminop = AdminUI.AdminInterface()
                            if(Adminop == "1"): #View Products
                                s.ClearScreen()
                                print("--------- View Products --------")
                                print("")
                                if len(Products_DL.productsList) > 0:
                                    Products_DL.ViewProducts()
                                    s.Getch()
                                else:
                                    print("No product added yet")
                                    s.Getch()
                            elif Adminop == "2": #Add Products
                                s.ClearScreen()
                                print("---------- Add Product ------------")
                                print("")
                                if len(Products_DL.productsList) > 0:
                                    Products_DL.ViewProducts()
                                products = AdminUI.TakeProductInputFromAdmin()
                                if products != None:
                                    Products_DL.AddInProductList(products)
                                    Products_DL.StoreProductsInfile(productpath)
                                    print("Product added successfully")
                                    s.Getch()
                                else:
                                    print("Invalid info added")
                                    s.Getch()
                            elif Adminop == "3": #delete products
                                s.ClearScreen()
                                print("-------- Delete Product -----------")
                                print("")
                                if len(Products_DL.productsList) > 0:
                                    Products_DL.ViewProducts()
                                    
                                name = input("Enter Product Name: ")
                                check = Products_DL.CheckProduct(name)
                                if check == True:
                                    index = Products_DL.ViewIndex(name)
                                    Products_DL.DeleteProducts(index)
                                    Products_DL.StoreProductsInfile(productpath)
                                    print("Product has been deleted successfully")
                                    s.Getch()
                                else:
                                    print("Product not found")
                                    s.Getch()
                            elif Adminop == "4": #change quantity
                                s.ClearScreen()
                                print ("---------- Change Quantity -------------")
                                print("")
                                if len(Products_DL.productsList) > 0:
                                    Products_DL.ViewProducts()
                                    
                                name = input("Enter Product Name: ")
                                check = Products_DL.CheckProduct(name)
                                if check == True:
                                    index = Products_DL.ViewIndex(name)
                                    newquantity = float(input("Enter new quantity: "))
                                    if newquantity > 0:
                                        Products_DL.ChangeQuantity(index, (newquantity))
                                        Products_DL.StoreProductsInfile(productpath)
                                        print("Quantity has been changed successfully")
                                        s.Getch()
                                    else:
                                        print("Invalid Quantity")
                                        s.Getch()
                                else:
                                    print("Product not found")
                                    s.Getch()
                        s.Getch()
                    elif(getrole == "User" or getrole == "user"):
                        s.ClearScreen()
                        uoption = None
                        while uoption != "8":
                            s.ClearScreen()
                            uoption =  CustUI.CustomerInterface()
                            if(uoption == "1"): # View Products
                                s.ClearScreen()
                                print("------------ View Prodcuts ------------")
                                if len(Products_DL.productsList) > 0:
                                    Products_DL.ViewProducts()
                                    s.Getch()
                                else:
                                    print("No product added yet")
                                    s.Getch()
                            elif uoption == "2": #Add to cart
                                s.ClearScreen()
                                print("----------- Add To Cart -------------")
                                if len(Products_DL.productsList) > 0:
                                    Products_DL.ViewProducts()
                                customerProducts = CustUI.CustomerProductInput(user.GetUsername())
                                if customerProducts != None:
                                    CustomerCart_DL.AddtoCart(customerProducts)
                                    CustomerCart_DL.StoreCustomerCart(customercart)
                                    print("Product has been added successfully")
                                    s.Getch()
                                # else:
                                #      print("Product Not Found")
                                #      s.Getch()
                            elif uoption == "3": # View carts
                                s.ClearScreen()
                                print("---------- View Cart ----------")
                                CustomerCart_DL.ViewCart(user.GetUsername())
                                s.Getch()
                            elif uoption == "4": #Delete product
                                s.ClearScreen()
                                print("------- Delete Product -----------")
                                CustomerCart_DL.ViewCart(user.GetUsername())
                                deleteproduct = input("Enter Product Name to Delete: ")
                                index = CustomerCart_DL.ViewCartIndex(deleteproduct, user.GetUsername())
                                if index >= 0:
                                    CustomerCart_DL.Deleteproduct(index)
                                    CustomerCart_DL.StoreCustomerCart(customercart)
                                    print("Your product has been deleted")
                                    s.Getch()
                                else:
                                    print("Product not found")
                                    s.Getch()
                            elif uoption == "5": # Change quantity
                                s.ClearScreen()
                                print("----------- Change Quantity ------------")
                                CustomerCart_DL.ViewCart(user.GetUsername())
                                productname = input("Enter Product name you want to change Quantity: ")
                                index = CustomerCart_DL.ViewCartIndex(productname , user.GetUsername())
                                if index >= 0:
                                    productquantity = float(input("Enter New Quantity: "))
                                    productPrice = Products_DL.GetProductPrice(productname)
                                    CustomerCart_DL.ChangeQuantity(index,productquantity, productPrice)
                                    CustomerCart_DL.StoreCustomerCart(customercart)
                                    print("Quantity has been updated successfully")
                                    s.Getch()
                                else:
                                    print("Error! Product not found")
                                    s.Getch()
                            elif uoption == "6": #clear cart
                                s.ClearScreen()
                                print("----------- Clear Cart -------------")
                                CustomerCart_DL.ViewCart(user.GetUsername())
                                op = input("Do you want to clear your cart(Y/N): ")
                                if op == 'Y' or op == 'y':
                                    userProductsIndexes = CustomerCart_DL.GetUserIndexes(user.GetUsername())
                                    if len(userProductsIndexes) > 0:
                                        CustomerCart_DL.ClearCart(userProductsIndexes)
                                        CustomerCart_DL.StoreCustomerCart(customercart)
                                        print("Your cart has been cleared")
                                        s.Getch()
                                    else:
                                        print("You don't have any product in your cart")
                                        s.Getch()
                                elif op == 'N' or op == 'n':
                                    print("Your operation has been cancelled")
                                    s.Getch()
                                else:
                                    print("Error! You entered wrong option..")
                                    s.Getch()
                            elif uoption == "7": # calculate Bill
                                s.ClearScreen()
                                print("--------- Total Bill -----------")
                                CustomerCart_DL.ViewYourFinalCart(user.GetUsername())
                                totalBill = CustomerCart_DL.GetTotalBill(user.GetUsername())
                                print("Total Bill: " , totalBill)
                                userProductsIndexes = CustomerCart_DL.GetUserIndexes(user.GetUsername())
                                if len(userProductsIndexes) > 0:
                                    CustomerCart_DL.ClearCart(userProductsIndexes)
                                CustomerCart_DL.StoreCustomerCart(customercart)
                                Products_DL.StoreProductsInfile(productpath)
                                s.Getch()
                        s.Getch()                 
                else:
                    print("User Not Found")
                    s.Getch()
                
                
        elif option == "2": # sign up
            user = SignUpUI.TakeInputWithRole()
            if user != None:
                check = MUser_DL.CheckUser(user)
                if check == False:
                    MUser_DL.AddInList(user)
                    MUser_DL.StoreUserInFile(userpath)
                    print("Sign Up successfully")
                    s.Getch()
                else:
                     print("User already exist")
                     s.Getch()
            else:
                print("Invalid Credentials")
                s.Getch()
                
        elif option == "3": # view user
            MUser_DL.ViewList()
            s.Getch()
    
    
if __name__ == "__main__":
    main()