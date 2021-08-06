#1. define a function called calc that inputs x, and RETURNS the y value of y=3x+4
def calc(x):
    return 3 * x + 4

#2. define a function called fahrenheit_to_celsius that inputs a float 'fahrenheit' and returns the celsius tempreture in float. 
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

#3. define a function called celsius_to_fahrenheit that converts a float 'celsius' to temperature fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

#4. define a function text_to_num that converts a string argument "text" into a float and returns it.  
def text_to_num(text):
    return float(text)

#5. define an add function which adds two objects from args (args is short for arguments) a and b together and returns it. 
def add(a, b):
    return a + b

#6. define a function called add_texts that asks the users via commandline for 2 texts and returns the texts added together. 
def add_texts():
    text1 = input("Text 1: ")
    text2 = input("Text 2: ")
    return text1 + text2

#7. define a function called get_height which takes no arguments, asks the user for their height via commandline and then returns the height as a float. 
def get_height():
    return float(input("Height: "))
def get_height():
    height = float(input("Height: "))
    return height
def get_height():
    height = input("Height: ")
    return float(height)
#all answers above are acceptable

#8. define a function get_temp_C that takes no arguments.
# it asks the user for the temperature in fahrenheit, 
# turns it into a float, 
# converts it into the temperatue in celsius (using the function fahrenheit_to_celsius function defined earlier),
# and returns the temperature in celsius
def get_temp_C():
    temp_F = float(input("Temp (Fº): "))
    temp_C = fahrenheit_to_celsius(temp_F)
    return temp_C

#9. define a function convert_F_to_C that takes no arguments,
# it asks the user for the temperature in Celsius, 
# turns it into a float, 
# converts it into the temperatue in fahrenheit (using the function celsius_to_fahrenheit function defined earlier),
# prints the temperature in celsius,
# and returns True (which represents executed successfully)

def convert_F_to_C():
    temp_C = float(input("Temp (Cº): "))
    temp_F = celsius_to_fahrenheit(temp_C)
    print("Temp (Fº) = " + temp_F)
    return True

#10. define a function called introduce that takes the string argument "name".
# It prints the introduction "Hello my name is {name}. I am currently 16. Nice to meet you!",
# and returns nothing
def introduce(name):
    print("Hello my name is " + name + ". I am currently 16. Nice to meet you!")

def introduce(name):
    print("Hello my name is " + name + ". I am currently 16. Nice to meet you!")
    return None #this line is not necessary as if you don't add the return statement it won't return anything anyways. 
