import time as t

password = "password123"
is_logged_in = False
attempt_count = 0
message = "Super secret message"


while not is_logged_in:
    p = input("Password: ")
    attempt_count += 1

    if p == password:
        is_logged_in = True
    else:
        print("Incorrect password (" + str(attempt_count) + " attempt)" )
        if attempt_count == 3:
            print("Please wait 30 seconds before you can guess again")
            t.sleep(30)
            attempt_count = 0

print(message)