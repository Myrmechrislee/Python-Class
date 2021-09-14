import numpy
#lists
x = [1, 2, 3, 4]
shopping_list = ["eggs", "milk", "bread", "meth"] #called array or list
class_list = [
    "seongsoo",
    "chris",
    "danilo"
]

#while loop
idx = 0
while idx < len(shopping_list):
    print("shopping_list[" + str(idx) + "] = " + shopping_list[idx])
    idx += 1

# while idx < len(shopping_list):
#     print(shopping_list[idx])
#     break

# #forloop
for x in class_list:
    print(x + " is in Physics class")

# #loop statements
# for x in ["chris", "adrian", "danilo", "jake", "seongsoo"]:
#     if x == "chris":
#         break #stops the loop
#     elif x == "seongsoo":
#         continue # jump to next item
#     elif x == "danilo":
#         pass # does nothing, but prevents nothing code error. 
#     print(x)


#range
# print(list(range(1, 10)))
# print(list(range(10, 15)))
# print(list(range(15)))

# #solving points of graph
def f(x):
    return numpy.sin(x)

for n in range(-10, 11):
    print(f(n))


