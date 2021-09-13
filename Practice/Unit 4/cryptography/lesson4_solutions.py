import argon2, binascii

#1. create an empty list called database
database = []

#2. create a class UserAccount that has a name and passwordHash property. 
class UserAccount:
    def __init__(self, name: str, passwordHash: bytes):
        self.name = name
        self.passwordHash = passwordHash

#3. define a register_user function that stores the name and password hashed in the database. 
def register_user(name: str, password: str):
    database.append(UserAccount(name, argon2.PasswordHasher().hash(password)))
#4. define a login function that prints success when loged in and try again if failed. 
def login():
    account, password = None, None
    while password == None:
        try:
            name = input("Name: ")
            matches = list(filter(lambda x: x.name == name, database))
            if len(matches) > 0:
                a = matches[0]
                test = input("Password: ")
                argon2.PasswordHasher().verify(a.passwordHash, test)
                account, password = a, test
                print("Login success")
            else:
                print("Name not found")
        except argon2.exceptions.VerifyMismatchError as e:
            print("password not found, please try again")

register_user("Christophe", "password")
login()