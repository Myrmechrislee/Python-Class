#modules

#import file
import lesson2
print(lesson2.f1(1.1))

#renaming import
import lesson2 as math_functions
print(math_functions.f2(2.2))

#import localy
from lesson5 import chris
print(chris["name"])

#import built in modules
import time
print("I'll be back in 5 seconds")
time.sleep(5)
print("Hello!")

#dates
from datetime import date
birthdate = date(2004, 6, 2)
age = date.today().year - birthdate.year
print("I am currently " + age + " years old")

#documentation