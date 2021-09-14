import random

print("Think of a number between 1-100. ")
print()

guessed, maximum, minimum = False, 100, 0

while not guessed:
    guess = random.randint(minimum, maximum)
    response = input("Is the number higher, lower or equal to " + str(guess) + "? ") # "higher", "lower", "equal to"
    if response == "higher":
        minimum = guess + 1
    elif response == "lower":
        maximum = guess - 1
    elif response == "equal to":
        guessed = True

print("The number is " + str(guess))