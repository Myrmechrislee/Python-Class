#1. create a class Bike (pass with no methods or properties)
class Bike:
    pass

#2. create a class Banana (pass with no methods or properties)
class Banana:
    pass

#3. create a class Car (pass with no methods or properties)
class Car:
    pass

#4. a) create class Food with properties: sweetness, sourness, bittnerness and saltiness all set to 0
class Food:
    sweetness = 0
    sourness = 0
    bitterness = 0
    saltiness = 0

#4. b) create a subclass Apple that derives from Food. Sweetness set at 5 and sourness set at 3
class Apple(Food):
    sweetness = 5
    sourness = 3

#4. c) create a subclass Soup that derives from Food. Set saltiness at 2 and bitterness at 1. 
class Soup(Food):
    saltiness = 2
    bitterness = 1

#4. d) create a subclass PotatoSoup that derives from Soup. Set sweetness at 3 and bitterness at 0.5
class PotatoSoup(Soup):
    sweetness = 3
    bitterness = 0.5

#4. e) Make a 2 potato soups and save it under my_soup1 and my_soup2. The first soup had a bit of lemon juice in it, so the sourness is set to 1. 
my_soup1 = PotatoSoup()
my_soup1.sourness = 1

my_soup2 = PotatoSoup()

#4. f) what is the sweetness, sourness, bitterness and saltiness of both my_soup1 and mysoup2?
#my_soup1
print(my_soup1.sweetness)   # = 3
print(my_soup1.sourness)    # = 1, 1 because you set the sourness to 1 earlier. 
print(my_soup1.bitterness)  # = 0.5
print(my_soup1.saltiness)   # = 2

#my_soup2
print(my_soup2.sweetness)   # = 3
print(my_soup2.sourness)    # = 0
print(my_soup2.bitterness)  # = 0.5
print(my_soup2.saltiness)   # = 2

# 5. a) Create the following classes with the following properties
# i) Car; speed = 100, x_position = 0
class Car:
    speed = 100
    x_position = 0

# ii) Animal; name = "Unkown", size = 0
class Animal:
    name = "Unkown"
    size = 0

# iii) Person; name = "Unknown", birthdate = "Unkown", gender = None
class Person:
    name = "Unkown"
    birthdate = "Unkown"
    gender = None

# iv) UserAccount; username = "", email = "", phone = "", password = ""
class UserAccount:
    username = ""
    email = ""
    phone = ""
    password = ""

#5. b) For each of the following set a subclass with the following property overrides
# i) Formula1; speed = 2000
class Formula1(Car):
    speed = 2000
# ii) Dog; name = "Dog", size = 21
class Dog(Animal):
    name = "Dog"
    size = 21
# iii) MaleHuman; gender = "male"
class MaleHuman(Person):
    gender = "male"
# iv) Administrator; no change (pass)
class Administrator(UserAccount):
    pass

#6. Create classes with the folloing methods with no (pass)
# a) Car: addspeed with no args and get_position with arg time
class Car:
    def addspeed(self): # make sure to indent as this is a method which is nested in a class
        pass #indent twice as this is code nested within a method nested in a class
    def get_position(self, time):
        pass
# b) Animal: change_name with arg new_name, grow_taller with arg height
class Animal:
    def change_name(self, new_name):
        pass
    def grow_taller(self, height):
        pass
# c) Person: get_age no args, change_gender with arg gender
class Person:
    def get_age(self):
        pass
    def change_gender(self, gender):
        pass
# d) UserAccount: change_phone with arg phone and password, change_email with arg email and password, is_correct_password with arg password. 
class UserAccount:
    def change_phone(self, phone, password):
        pass
    def change_email(self, email, password):
        pass
    def is_correct_password(self, password):
        pass
# 6. a) Create a class called PhysicsObject with the following:
# Properties:
# - displacement        (s)
# - initial_velocity    (u)
# - final_velocity      (v)
# - time_passed         (t)
# - acceleration        (a)
# When initialised, it takes in the args: s, u, a, t and fills in all the properties (calculating final velocity) (remember v = u + at)
class PhysicsObject:
    def __init__(self, s, u, a, t):
        self.displacement = s
        self.initial_velocity = u
        self.time_passed = t
        self.acceleration = a
        self.final_velocity = u + a * t
# 6. b) save a PhysicsObject with the displacement (s) of 0, initial velocity (u) of 0, acceleration (a) of -9.8 and 6 seconds passed, saved under falling_carrot. 
falling_carrot = PhysicsObject(0, 0, -9.8, 6) 

# 6. c) print the final velocity of the falling_carrot
print(falling_carrot.final_velocity) # -58.8

# 7. a) create class called UserAccount that has the initialising args name, password, birthyear. When initialising, it saves the properties name, password, birthyear and age (2021 - birthyear). 
class UserAccount:
    def __init__(self, name, password, birthyear):
        self.name = name
        self.password = password
        self.birthyear = birthyear
        self.age = 2021 - birthyear
# 7. b) add a method called introduce which prints in the format "Hello my name is {name}, I was born in the year {birthyear} and I am currently {age} years old. "
class UserAccount:
    def __init__(self, name, password, birthyear):
        self.name = name
        self.password = password
        self.birthyear = birthyear
        self.age = 2021 - birthyear
    def introduce(self):
        print("Hello my name is " + self.name + ", I was born in the year " + str(self.birthyear) + " and I am currently " + str(self.age) + " years old. ")
# 7. c) create UserAccount with the name John, password is 1234 (string), and birthyear of 1999 and run the introduce method. 
john = UserAccount("John", "1234", 1999)
john.introduce()
#or
UserAccount("John", "1234", 1999).introduce()

# 7. d) Create a subclass BankAccount that derived from the base class UserAccount. 
# When initialising, it takes all the args of UserAccount and takes an extra one which is balance. 
# The __init__ function initialises the old class and adds a new property balance. 
class BankAccount(UserAccount):
    def __init__(self, name, password, birthyear, balance):
        super().__init__(name, password, birthyear)
        self.balance = balance
# 7. e) add a new method to the BankAccount class called calculate_tax which takes in arg tax_rate (as a float representing the percentage) and returns the amount of tax owed. 
class BankAccount(UserAccount):
    def __init__(self, name, password, birthyear, balance):
        super().__init__(name, password, birthyear)
        self.balance = balance
    def calculate_tax(self, tax_rate):
        return self.balance * tax_rate / 100

# 7. f) add a new method called deduct_tax which takes the argument tax_rate (as a float representing the percentage), calculates the amount of tax owed (you can use the function defined earlier by using self.calculate_tax) and removes it from the account balance. 
class BankAccount(UserAccount):
    def __init__(self, name, password, birthyear, balance):
        super().__init__(name, password, birthyear)
        self.balance = balance
    def calculate_tax(self, tax_rate):
        return self.balance * tax_rate / 100
    def deduct_tax(self, tax_rate):
        owed = self.calculate_tax(tax_rate)
        self.balance -= owed
# 7. g) 
# i) Create a Bank account for Aron who has the password 4321 (string), born in the year 2000 and has $1,000 saved under the variable account. 
account = BankAccount("Aron", "4321", 2000, 1000)
# ii) Print his balance and tax owed, assuming the tax rate for him is 10%
print("Balance: $" + str(account.balance))
print("Tax Owed: $" + str(account.calculate_tax(10)))
# iii) Deduct the tax, assuming the tax rate for him is 10%
account.deduct_tax(10)
# iv) Print his new balance
print("New Balance: $" + str(account.balance))

# 8. a) Create a class called Person that initialises with the properties set from the arguments: name, birthyear, gender and calculate the property age. 
class Person: 
    def __init__(self, name, birthyear, gender):
        self.name, self.birthyear, self.gender = name, birthyear, gender #short hand of self.name = name...
        self.age = 2021 - birthyear
# 8. b) Some people may chose to write random genders or make typos. Create an if statement for when the gender is not Male of Female in the __init__, it would automatically set it to Male. 
class Person: 
    def __init__(self, name, birthyear, gender):
        self.name, self.birthyear = name, birthyear #short hand of self.name = name...
        self.age = 2021 - birthyear
        if (not gender == "Male") and (not gender == "Female"):
            self.gender = "Male"
        else:
            self.gender = gender
# 8. c) Add a function introduce that takes no arguments and prints the format "Hello, my name is {name}. I am a {gender}. I am {age} years old born in the year {birthyear}. "
class Person: 
    def __init__(self, name, birthyear, gender):
        self.name, self.birthyear = name, birthyear
        self.age = 2021 - birthyear
        if (not gender == "Male") and (not gender == "Female"):
            self.gender = "Male"
        else:
            self.gender = gender
    def introduce(self):
        print("Hello, my name is " + self.name + ". I am a " + self.gender + ". I am " + str(self.age) + " years old born in the year " + str(self.birthyear) + ". ")

# 8. d) Create the following people and save it in a list called database:
# Name: Ben, Gender: Male, Birthdate: 2000
# Name: Caroline, Gender: Female, Birthdate: 1999
# Name: Daniel, Gender: Male, Birthdate: 2004
# Name: Eli, Gender: Male, Birthdate: 2005
# Name: Fiona, Gender: Female, Birthdate: 1968
# Name: Greg, Gender: Male, Birthdate: 1969
# Name: Henry, Gender: Male, Birthdate: 2001
# Name: India, Gender: Female, Birthdate: 2004
# Name: Jacqueline, Gender: Female, Birthdate: 1968
# Name: Kevin, Gender: Male, Birthdate: 2003
database = [
    Person("Ben", 2000, "Male"),
    Person("Caroline", 1999, "Female"),
    Person("Daniel", 2004, "Male"),
    Person("Eli", 2005, "Male"),
    Person("Fiona", 1968, "Female"),
    Person("Greg", 1969, "Male"),
    Person("Henry", 2001, "Male"),
    Person("India", 2004, "Female"),
    Person("Jacqueline", 1968, "Female"),
    Person("Kevin", 2003, "Male")
]
# 8. e) i) Create a new list 'males'. Using a 'for' loop and list.append function, add all the males from the database into the males list. 
males = []
for person in database:
    if(person.gender == "Male"):
        males.append(person)

#8. e) ii) Make all the males introduce themselves. 
for person in males:
    person.introduce()

# 8. f) i) Create a new list 'after_2000'. Using a 'for' loop and list.append function, add all the people born after the year 2000 from the database into the after_2000. 
after_2000 = []
for person in database:
    if(person.birthyear > 2000):
        after_2000.append(person)
#8. f) ii) Make all the after_2000's introduce themselves. 
for person in after_2000:
    person.introduce()
# 8. g) i) Create a new list 'adults'. Using a 'for' loop and list.append function, add all the people who are 18 or above in age from the database into the adults. 
adult = []
for person in database:
    if(person.age >= 18):
        adult.append(person)
#8. g) ii) Make all the adults introduce themselves. 
for person in adult:
    person.introduce()

#8. h) i) Define a function called add_person which takes the arguments name, gender and birthyear and adds the person to the database. (using list.append function)
def add_person(name, gender, birthyear):
    database.append(Person(name, birthyear, gender)) # the arguments setup for the class is orded differently

#8. h) ii) Add the following people using the add person function
# Name: Leo, Gender: Male, Birthdate: 2004
# Name: Liam, Gender: Male, Birthdate: 2004
# Name: Lukas, Gender: Male, Birthdate: 2004
add_person("Leo", "Male", 2004)
add_person("Liam", "Male", 2004)
add_person("Lukas", "Male", 2004)

#8. h) iii) Now introduce all the males including the new ones. 
males = []
for person in database:
    if(person.gender == "Male"):
        males.append(person)

for person in males:
    person.introduce()

#or
for person in database:
    if(person.gender == "Male"):
        person.introduce() # no need to define a list. 
