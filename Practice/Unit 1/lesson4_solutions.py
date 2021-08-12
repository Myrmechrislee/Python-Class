# 1. create a list called animals with the strings: zebra, elephant, dog, cat, mouse, fish

animals = ["zebra", "elephant", "dog", "cat", "mouse", "fish"]

# 2. create a list called fruits with the strings: apple, banana, grapes

fruits = ["apple", "banana", "grapes"]

# 3. create a list called x with the integers: 1, 2, 4, 5, 6

x = [1, 2, 4, 5, 6]

# 4. create a list called y with the integers: 9, 4, 2, 7, 1

y = [9, 4, 2, 7, 1]

# 5. A matrix can be created by using a list of lists of numbers such as floats or ints. 
# For example, 
# matrix:   [ 1 4 3 ]
#           [ 1 2 1 ]
#           [ 1 7 0 ]
# would be saved as matrix = [
#   [1, 4, 3],
#   [1, 2, 1],
#   [1, 7, 0]
# ]
# or matrix = [[1, 4, 3], [1, 2, 1], [1, 7, 0]]
# now construct matrix a that contains the following data:
#   [ 0 1 0 0 1 ]
#   [ 1 0 1 0 0 ]
#   [ 0 1 0 1 0 ]
#   [ 1 0 1 0 1 ]
#   [ 1 1 1 1 0 ]

a = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0]
] # you can do multiple lines for easier readibility however it can also be set in a single line
a = [[0, 1, 0, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [1, 1, 1, 1, 0]]

# 6. create a loop that runs function login with no arguments while not is_logged_in
is_logged_in, login = True, lambda: None
while not is_logged_in:
    login()

# 7. create loop that runs function lower_temp() while temp is above 27. 
temp, lower_temp = 0, lambda: None
while temp > 27:
    lower_temp()

# 8. a) define a variable eggs to the int 7
eggs = 7

# 8. b) create a variable egg_count and set it to 0
egg_count = 0

# 8. c) create a while loop for while eggs is greater than 0, add 1 to egg_count and minus one from eggs
while eggs > 0:
    egg_count += 1 # this is the same as eggcount = egg_count + 1
    eggs -= 1 # this is the same as eggs = eggs - 1

#at the end this loop, the code would have counted all the eggs.
# 8. d) print the amount of eggs
print("The amount of eggs is: " + str(egg_count))

# 9. Print the length of the array animals (defined in Q1, use the len function)
print("The length of the animals array is " + str(len(animals)))

# 10. Print the length of the array fruits (defined in Q2)
print("The length of the fruits array is " + str(len(fruits)))

# 11. a) Print the amount of rows of the matrix a (defined in Q3)
print("The rows of the matrix a is " + str(len(a)))

# 11. b) Print the amount of columns in matrix a (defined in Q3)
print("The columns of the matrix b is " + str(len(a[0])))

# 11. c) A square matrix is when rows == columns. Create a function is_square_matrix that takes is arg matrix and returns True if it is a square matrix or False if matrix is not a square matrix. 
def is_square_matrix(matrix):
    return len(matrix) == len(matrix[0])

# 12. a) create a shopping_list list with the string values eggs, milk, boxes, bread. 
shopping_list = ["eggs", "milk", "boxes", "bread"]

# 12. b) What would the value of shopping_list[1] be?
shopping_list[1] # = milk
# rememebr the array starts from 0

# 12. c) What would the value of shopping_list[4] be?
shopping_list[4] #=  Out of range error because index of 4 is outside the list

# 12. d) Using a for loop, print each of the items of the shopping_list on a new line with the format " - {item}". 
for item in shopping_list:
    print(" - " + item)

# 13. e) Print a numbered list (format "{n}. {item}") for shopping_list. (hint: define idx = 0 outside the loop)
idx = 0
for item in shopping_list:
    idx += 1 # if idx is added before printing then you don't need to add one when printing. 
    print(str(idx) + ". " + item)

# or 
idx = 0
for item in shopping_list:
    print(str(idx + 1) + ". " + item)
    idx += 1

# or you can use enumerate function
for idx, item in enumerate(shopping_list):
    print(str(idx + 1) + ". " + item)

# 14. Create a range between 0 - 10 saved under k
k = range(0, 11)

# 15. Create a range between 1 - 20 saved under l
l = range(1, 21)

# 16. Create a range between 1-100 saved under m
m = range(1, 101)

# 17. Create a range between 1-52 saved under n
n = range(1, 53)

# 18. Create a function make_span with args min, max and returns a range between the min and max (including min and max). 
def make_span(min, max):
    return range(min, max+1)

# 19. a) Create a range between 1-31 saved under days
days = range(1, 32)
# 19. b) Times each of the values by 16.25 (money earned) and add each value to a new list total_income. (add a value in a list by using {list}.append({value}) function)
total_income = []
for day in days:
    total_income.append(day * 16.25)
# 19. c) That is the total amount of money you earn each day. For each day print out the income in the format "Day {n}: ${income}". 
n = 0
for income in total_income:
    n += 1
    print("Day " + str(n) + ": $" + str(income))

#or you can use enumerate function
for n, income in enumerate(total_income):
    print("Day " + str(n + 1) + ": $" + str(income))

# 20. Karren's income for each week of a month is as follows: $91.21, $31.72, $61.42, $72.00
# a) Save this under a list: weekly_income. 
weekly_income = [91.21, 31.72, 61.42, 72.00]
# b) She saves 10% for her savings and spends $20 on shopping each week. Save the remaining of each week in a new list weekly_leftover. (Remember to add a value to a list use {list}.append({value}) function)
weekly_leftover = []
for income in weekly_income:
    weekly_leftover.append(income * 0.9 - 20)
# c) Print the total amount of money she has remaining. 
remaining = 0
for left in weekly_leftover:
    remaining += left
print("Karren has $" + str(remaining) + " left over. ")

# 21.
# a) Define a function f which takes arg x and returns the y value of y = x ^ 2 - 4
def f(x):
    return x ** 2 - 4

# b) Print the values of f(x) when x between [-10, 10] in point form (format "({x}, {f(x)})"). 
for x in range(-10, 11):
    print("(" + str(x) + ", " + str(f(x)) + ")")

