import os
class Menu:
    @staticmethod
    def MenuLogin():
        print("1. Sign In")
        print("2. Sign Up")
        print("3. View Users")
        print("4. Exit")
        print("--------------------")
        option = input("Select Your option: ")
        return option
    
    @staticmethod
    def ClearScreen():
        os.system("cls")
        
    @staticmethod
    def Getch():
        input("Press any key to Continue...")