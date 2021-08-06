# 1. what is 10 (0b1010) & 12 (0b1100)?

10 & 12 # = 8

# 2. what is 15 (0b1111) & 16 (0b10000)?

15 & 16 # = 0

# 3. what is 18 (0b10010) & 20 (0b10100)?

18 & 20 # = 16

# 4. what is 30 (0b11110) | 35 (0b100011)?

30 | 35 # = 63

# 5. what is 26 (0b11010) | 35 (0b100011)?

26 | 35 # = 59

# 6. what is 123 (0b1111011) | 143 (0b10001111)?

123 | 143 # = 255

# 7. what is 26 (0b11010) ^ 35 (0b100011)?

26 ^ 35 # = 57

# 8. what is 85 (0b1010101) ^ 97 (0b1100001)?

85 ^ 97 # = 52

# 9. what is 30 (0b11110) ^ 35 (0b100011)?

30 ^ 35 # = 61

# 10. what is 17 (0b10001) ^ 24 (0b11000)?

17 ^ 24 # = 9

# 11. translate if christophe_age is 17 then run() to code. 
if christophe_age == 17:
    run() #indentation is very important. It shows that the function is nested inside the if statement. 

# 12. translate to code: if banana_age is less than apple_age then print "Banana is younger", otherwise print "apple is younger"
if banana_age < apple_age:
    print("Banana is younger")
else:
    print("apple is younger")

#13. translate to code: if jenny_age is less than or equal to 4 then run function block with argument "Jenny",
# otherwise, if jenny_age is less than 12, run function warn with argument "Jenny",
# otherwise run function allow with argument "Jenny". 
if jenny_age <= 4:
    block("Jenny")
elif jenny_age < 12:
    warn("Jenny")
else:
    allow("jenny")

#14. translate to code: if height is less than 160, print "Short".
# or else, if height is less than 190, print "Average".
# otherwise, print("Tall")
if height < 160:
    print("Short")
elif height < 190:
    print("Average")
else:
    print("Tall")

#15. Define a function f1 with argument x.
# If x is less than or equal to -2, return the y value of y=2x - 3
# Otherwise if x is less than 0, return y value of y=(x - 3) ^ 2 - 3
# Otherwise if x is less than 5, return y value of y=-x^2 + 3
# otherwise, return the y value of y=-5x + 3
def f1(x):
    if x <= -2:
        return 2 * x - 3 # double indent because the return statement is nested inside the if statement which is nested inside the function. 
    elif x < 0:
        return (x - 3) ** 2 - 3
    elif x < 5: # you can use multiple elif statements, however you can only use 1 if and else statement in each thread of conditions. 
        return x ^ 2 + 3
    else:
        return -5 * x + 3

#16. Define a function login that takes no args. 
# The function asks the user via commandline for a password. 
# If the password is "buzz123" then print "Welcome", otherwise print("Incorrect password") and run login again. 
def login():
    password = input("Password: ")
    if password == "buzz123":
        print("Welcome")
    else:
        print("Incorrect password")
        login() # both print and login are double indented because they are nested in the else statement which is nested in the login function. 

#17. Define a function called ask_age with the arg return_type. 
# The function first asks the user for their age. 
# If return_type is "string" then return the age as string. 
# Otherwise if return_type is "float", return age as a float. 
# Otherwise if return_type is "none", return None. 
# Otherwise, return age as an int. 
def ask_age(return_type):
    age = input("Age: ")
    if return_type == "string":
        return age # there is no need to write str(age) because the input function originally returns a string
    elif return_type == "float":
        return float(age)
    elif return_type == "none":
        return None
    else:
        return int(age)

#18. Define a function called compare_types with args a and b. 
# if the type of a is NOT the same as the type of b, print "a is not the same type as b" (use the type function to find the type of an object)
# otherwise, print "a is the same type as b"

def compare_types(a, b):
    if not type(a) == type(b):
        print("a is not the same type as b")
    else:
        print("a is the same type as b")

#19. Define a function called is_inside_rect that takes the the args rect_x, rect_y, rect_width, rect_height, x, y. 
# If x is greater than the left bound of the rect (rect_x - rect_width / 2) and less than the right bound of the rect (rect_x + rect_width / 2),
# and y is greater than the lower bound of the rect (rect_y - rect_height / 2) and less than the upper bound of the rect (rect_y + rect_height / 2),
# then print "x is inside the rectangle" and return True
# otherwise print "x is outside the rectangle" and return False
def is_inside_rect(rect_x, rect_y, rect_width, rect_height, x, y):
    upper_bound = rect_y + rect_height / 2
    lower_bound = rect_y - rect_height / 2
    right_bound = rect_x + rect_width / 2
    left_bound = rect_x - rect_width / 2 # declaring them as variables makes it easier to read but is not required. 
    if x > left_bound and x < right_bound and y > lower_bound and y < upper_bound:
        print("x is inside the rectangle")
        return True
    else:
        print("x is outside the rectangle")
        return False
def is_inside_rect(rect_x, rect_y, rect_width, rect_height, x, y):
    if x > rect_x - rect_width / 2 and x < rect_x + rect_width / 2 and y > rect_y - rect_height / 2 and y < rect_y + rect_height / 2:
        print("x is inside the rectangle")
        return True
    else:
        print("x is outside the rectangle")
        return False


#20. Create a function called compare_names which takes the arguments, name1 and name2. 
# If name 1 is the NOT the same as name 2 check then run the following:
# - print name 1 is are the same 
# - If name 1 is longer than name 2 (use len function to find the length of the names), print "name 1 is longer than name 2".
# - else, if name 1 and 2 are the same length, print "name 1 and name 2 are the same length".
# - else print "name 2 is longer than name 1"
# otherwise, print "name 1 and name 2 are the same"
def compare_names(name1, name2):
    if not name1 == name2:
        print("name 1 is are the same as name 2")
        if len(name1) > len(name2):
            print("name 1 is longer than name 2")
        elif len(name1) == len(name2):
            print("name 1 and name 2 are the same length")
        else:
            print("name 2 is longer than name 1")
    else:
        print("name 1 and name 2 are the same")