# booleans and logic operations

# binary
a = True
b = False

print("type(a)=" + str(type(a)))
print("type(b)=" + str(type(b)))

#binary
0 == 0b0
1 == 0b1
2 == 0b10
3 == 0b11
4 == 0b100
5 == 0b101
6 == 0b110
7 == 0b111
8 == 0b1000
#...

# comparisons
x = 10
y = 30

print("x > y = " + str(x > y))
print("x < y = " + str(x < y))
print("x == y = " + str(x == y))

x = 10
y = 10
print("x == y = " + str(x == y))

#operators
a = True
b = False
c = True

print("a and b = " + str(a and b))
print("a or b = " + str(a or b))
print("not a = " + str(not c))
print()
print("a and b or c = " + str(a and b or c))
print("a xor b = " + str(a ^ b))
print("5 and 6 = 0b101 and  0b110 = " + str(5 & 6))


#conditions
chris_age = 17
seongsoo_age = 16
if True:
    print("a is true")
if 3 == 3:
    print("3 == 3 (true)")

if chris_age == 16:
    print("Christophe is 16 years old! (old)")
else:
    print("Christophe is not 16 boo")

if seongsoo_age == 16:
    print("you are the right age")
elif seongsoo_age < 16:
    print("sorry, you are too young")
else:
    print("sorry you are too old")

if seongsoo_age <= chris_age:
    print("Seongsoo is either younger or the same age as Christophe")
    if seongsoo_age < chris_age:
        print("seongsoo is younger than chris")
    else:
        print("seongsoo is the same age")
else:
    print("Seongsoo is older than Christophe")

