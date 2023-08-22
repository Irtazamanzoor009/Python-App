
from SignUpBL import SignUp_BL
class SignUp_UI:
    
    @staticmethod
    def TakeInputWithRole():
        name = input("Enter Name: ")
        password = input("Enter Password: ")
        role = input("Enter Role: ")
        if name != None and password != None and role != None:
            user = SignUp_BL(name, password, role)
            return user
        else:
            return None