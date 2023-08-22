from SignInBL import SignIn_BL

class SignIn_UI:
    
    @staticmethod
    def TakeInputWithoutRole():
        name = input("Enter Name: ")
        password = input("Enter Password: ")
        if name != None and password != None:
            user = SignIn_BL(name,password)
            return user
        else:
            return None