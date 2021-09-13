# 1. what is the type of 902903 ?
print(type(902903)) # = <class 'int'>

# 2. what is the type of 902.1 ?
print(type(902.1)) # = <class 'float'>

# Scientiffic notation are all floats

# 3. what is the type of 1e+91 ? 
print(type(1e+91)) # = <class 'float'>

# 4. what is the type of -10 ?
print(type(-10)) # = <class 'int'>

# 5. what is the type of -10.0 ?
print(type(-10.0)) # = <class 'float'>

# 6. what is the type of "101"
print(type("101")) # = <class 'str'>

# 7. what is the type of "-10"
print(type("-10")) # = <class 'str'>

# 8. what is the type of "adambaker@gmail.com"?
print(type("adambaker@gmail.com")) # = <class 'str'>

# 9. what is the type of 417976389?
print(type(417976389)) # = <class 'int'>

# 10. what is the type of "0417 976 389"?
print(type("0417 976 389")) # = <class 'str'>

# 11. what is the type of print ?
print(type(print)) # = <class 'builtin_function_or_method'>

# 12. the speed of light is 3*10^8 m/s. Store that in a variable called c. 
c = 3*10**8

# 13. i) the acceleration of gravity is -9.8 m/s. Store that in a variable g and state its type. 
g = -9.8
print(type(g)) # = <class 'float'>

#13. ii) save velocity of an object falling after 8 seconds as variable v (v=a*t). 
# Print its type and value
v = g * 2
print(type(v), v) # <class 'float'> -19.6
# or
print(type(v)) # <class 'float'>
print(v) #-19.6

# 14. what is the type of str(-10)?
print(type(str(-10))) # <class 'str'>

# 15. what is the type of int("1973")?
print(type(int("1973"))) #<class 'int'>

# 16. what is the type of float("13")?
print(type(float("13"))) # <class 'float'>

# 17. what is the type of int(12.2)?
print(type(int(12.2))) # <class 'int'>

# 18. Will int("12.2") produce an error? Why or why not?
# yes, as int cannot store values with decimal points but 12.2 has decimal value. 

# 19. Will float("johnny smith") produce an error? Why or why not?
# yes, as "johnny smith" cannot be changed to a number value. 

# 20. Why can't you use the operator "+" with "hello world" and 3?
# you cannot add a string and a int value. 
# you cannot add objects with different types. 

# 21. Ask the user, "What is your favourite colour? ". 
input("What is your favourite colour? ")

# 22. Ask the user, "What is 1+1? ". 
input("What is 1+1? ")

# 23. i) Ask the user, "what is your height? " and save the response to the variable "response". 
response = input("What is your height? ")

# 23. ii) what is the type of "response"? 
print(type(response)) # <class 'str'>

# 23. iii) convert "response" to float and save it as height. 
height = float(response)

# 24. the distance between the earth and the sun is 150.51*10^9 metres away from the sun. 
# 24. i) what data type would you store that value under?
# float

# 24. ii) set variable "d" to that value
d = 150.51*10**9

# 24. iii) ask the user for "Rocket Ship Speed (m/s): ", and save it under the variable "response". 
response = input("Rocket Ship Speed (m/s): ")

# 24. iv) what is the data type of "response"?
print(type(response)) # <class 'str'>

# 24. v) save variable "v" as a float of the speed of the rocket. (float(data)->float)
v = float(response)

# 24. vi) save variable "t" as the time it would take for the rocket to reach the sun. (t = d/v)
t = d/v

# 24. vii) what is the type of "t"?
print(type(t)) # <class 'float'>

# 24. viii) print in the format "it will take your rocket (t) seconds to reach the sun". 
print("it will take your rocket " + str(t) + " seconds to reach the sun")

# 24. ix) test your program. 
#run "python3 lesson1.py" on the commandline
