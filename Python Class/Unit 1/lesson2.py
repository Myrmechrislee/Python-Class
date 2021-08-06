def hello():
    print("hello")

def f1(x):
    return x**3 + x ** 2 + 3 * x + 7

def f2(x):
    return f1(x) / x

def print_f2(x):
    print(f2(4))

def do_somthing():
    x = float(input("Choose any number: "))
    print_f2(x)
    print("Done!")
    
