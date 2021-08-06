#objects and classes

#revision
text = str("13")
number = int(text)

#objects
seongsoo = {
    "name": "Kim Seongsoo",
    "age": None,
    "birthdate": "19/9/2004"
}
chris = {
    "name": "Christophe Lee",
    "age": 17,
    "birthdate": "02/06/2004"
}
dog = {
    "owner": chris,
    "age": 7,
    "eats": [ "cats", "sausages", "meat" ]
}

print("the dog is " + str(dog["age"]) + " years old with an owner " + str(dog["owner"]["age"]) + " years old. ")

#class
class Animal: # cookie cutter analogy
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.birthyear = 2021 - age
        self.call_type = "Silence"

    def introduce(self):
        print("Hi my name is " + self.name + ", I am " + str(self.age) + " years old born in the year " + str(self.birthyear) + ". I am a " + self.gender)
    
    def call(self):
        print(self.call_type)

my_cat = Animal("Chocolate", "toaster", 16)
my_cat.introduce()

my_cat.call_type = "meow"
my_cat.call()
my_cat.call()

# #derivative/inherit/subclass class
class Dog(Animal): # base class is Animal
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age) # creates the base class
        self.call_type = "bark"

my_dog = Dog("Benji", "male", 15)
my_dog.introduce()
my_dog.call()