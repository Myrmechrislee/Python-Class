#scopes

#inner and outer scope
outer_x = 1

def foo_bar():
    print(outer_x)

def foo_bar2():
    inner_x = 2 # inside function
    print(inner_x)
    
def foo_bar3():
    print(inner_x)

#'global' keyword
def test1():
    global global_y
    global_y = 0
    print(global_y)

def test2():
    print(global_y)

#lambda
f = lambda x: x ** 2 + 2 * x + 3
f(1)

def f1(x):
    return x ** 2 + 2 * x + 3