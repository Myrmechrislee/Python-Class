# 1. a) import the functions defined in lesson 2 as l2
import lesson2_solutions as l2 # You can use lesson2 instead
# 1. b) run function get_temp_C and print the temperature. 
temp_C = l2.get_temp_C()
print("The tempterature in Celsius is " + str(temp_C) + "ºC")

# 2. Fix the following code:
# temp = 0
# def find_temp():
#     temp = l2.get_temp_C()

# def show_temp():
#     find_temp()
#     print("the temp in C is " + str(temp))

# show_temp()

temp = 0
def find_temp():
    global temp
    temp = l2.get_temp_C()

def show_temp():
    find_temp()
    print("the temp in C is " + str(temp))

show_temp()

# 3. a) Create a class Rectangle with the properties x, y, width and height and set them with init args. 
class Rectangle:
    def __init__(self, x, y, width, height) -> None:
        self.x, self.y, self.width, self.height = x, y, width, height
# 3. b) using the is_inside_rect function defined in lesson3. Add a is_inside method with args x, y to the class
import lesson3_solutions as l3 # you would write import lesson3 instead
class Rectangle:
    def __init__(self, x, y, width, height) -> None:
        self.x, self.y, self.width, self.height = x, y, width, height
    def is_inside(self, x, y):
        l3.is_inside_rect(self.x, self.y, self.width, self.height, x, y)
#3. d) Ask the user for the dimentions of the rectangle (x, y, width, height) and save it under my_rect
my_rect = Rectangle(float(input("RECT X: ")), float(input("RECT Y: ")), float(input("RECT WIDTH: ")), float(input("RECT HEIGHT: ")))

#3. e) Ask the user for an x and y point and print whether it is inside or out of the rectangle
x, y = float(input("X: ")), float(input("Y: "))
my_rect.is_inside(x, y) # the function already prints for you. 

#4. Using the list defined in remaining money found in module 4 (variable: remaining), print the percentage of remaining to the total (find total by adding all of weekly_income). 
from lesson4_solutions import remaining, weekly_income # you would be doing "from lesson4 import..." instead
total = 0
for income in weekly_income:
    total += income # find the total amount of income

print("Remaining/Total = " + str(remaining / total * 100) + "%")

# 5. a) Import the BankAccount class and the database variable from lesson5
from lesson5_solutions import BankAccount, database # you would be doing "from lesson5 import..." instead

#5. b) create a new list called bankDB, and for each of the people in database, make them a bank account (set all the passwords to "password" and balance to $0.00) and save it to bankDB. 

bankDB = []
for person in database:
    bankDB.append(BankAccount(person.name, "password", person.birthyear, 0.00))

#5. c) create a function called get_account with args name, that finds the bank account of a person in bankDB with the name of name argument. 
def get_account(name):
    match = None
    for account in bankDB:
        if(account.name == name):
            match = account
    return match #answers may vary. you can test your function by running print(get_account("Jacqueline")). 

#5. d) create a function called is_correct_password which takes the args name and password. The function uses the function get_account to get the account and returns True if the passwords match, else false. 
def is_correct_password(name, password):
    return get_account(name).password == password #most efficient code, the comparison returns True if match or else false
#or
def is_correct_password(name, password):
    account = get_account(name)
    return account.password == password
#or
def is_correct_password(name, password):
    account = get_account(name)
    if account.password == password:
        return True
    else:
        return False # this also works but adding an if statement is unnessesary. 

#5. e) i) Ben wishes to log in using his name "Ben" and the password "Password". Print "Logged in!", if the password if correct or "Incorrect password" if the password is incorrect. 
if is_correct_password("Ben", "Password"):
    print("Logged in!")
else:
    print("Incorrect password") # prints incorrect
#5. e) ii) Ben forgets his to put his password to lowercase try the if statement again with the password "password". 
if is_correct_password("Ben", "password"):
    print("Logged in!") # prints logged in. 
else:
    print("Incorrect password")