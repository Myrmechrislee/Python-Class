# 1. create a list called animals with the strings: zebra, elephant, dog, cat, mouse, fish

# 2. create a list called fruits with the strings: apple, banana, grapes

# 3. create a list called x with the integers: 1, 2, 4, 5, 6

# 4. create a list called y with the integers: 9, 4, 2, 7, 1

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

# 6. create a loop that runs function login with no arguments while not is_logged_in
is_logged_in, login = False, lambda: None

# 7. create loop that runs function lower_temp() while temp is above 27. 
temp, lower_temp = 0, lambda: None

# 8. a) define a variable eggs to the int 7

# 8. b) create a variable egg_count and set it to 0

# 8. c) create a while loop for while eggs is greater than 0, add 1 to egg_count and minus one from eggs

#at the end this loop, the code would have counted all the eggs.
# 8. d) print the amount of eggs

# 9. Print the length of the array animals (defined in Q1, use the len function)

# 10. Print the length of the array fruits (defined in Q2)

# 11. a) Print the amount of rows of the matrix a (defined in Q3)

# 11. b) Print the amount of columns in matrix a (defined in Q3)

# 11. c) A square matrix is when rows == columns. Create a function is_square_matrix that takes is arg matrix and returns True if it is a square matrix or False if matrix is not a square matrix. 

# 12. a) create a shopping_list list with the string values eggs, milk, boxes, bread. 

# 12. b) What would the value of shopping_list[1] be?

# 12. c) What would the value of shopping_list[4] be?

# 12. d) Using a for loop, print each of the items of the shopping_list on a new line with the format " - {item}". 

# 13. e) Print a numbered list (format "{n}. {item}") for shopping_list. (hint: define idx = 0 outside the loop)

# 14. Create a range between 0 - 10 saved under k

# 15. Create a range between 1 - 20 saved under l

# 16. Create a range between 1-100 saved under m

# 17. Create a range between 1-52 saved under n

# 18. Create a function make_span with args min, max and returns a range between the min and max (including min and max). 
def make_span(min, max):
    return range(min, max+1)

# 19. a) Create a range between 1-31 saved under days
# 19. b) Times each of the values by 16.25 (money earned) and add each value to a new list total_income. (add a value in a list by using {list}.append({value}) function)
# 19. c) That is the total amount of money you earn each day. For each day print out the income in the format "Day {n}: ${income}". 

# 20. Karren's income for each week of a month is as follows: $91.21, $31.72, $61.42, $72.00
# a) Save this under a list: weekly_income. 
# b) She saves 10% for her savings and spends $20 on shopping each week. Save the remaining of each week in a new list weekly_leftover. (Remember to add a value to a list use {list}.append({value}) function)
# c) Print the total amount of money she has remaining. 

# 21.
# a) Define a function f which takes arg x and returns the y value of y = x ^ 2 - 4

# b) Print the values of f(x) when x between [-10, 10] in point form (format "({x}, {f(x)})")

