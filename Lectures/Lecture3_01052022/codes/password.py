password = ""

num_attempt = 0

while num_attempt < 3:
    password = eval(input("Enter password: "))
    if 10 <= password <= 99 and password % 2 == 0 and password//10%2 == 0:
        print("Validated!")
        exit()
    else:
        print("Invalid! try again!")
        num_attempt += 1
        if num_attempt == 3:
            print("Too many invalid attemps! Try again later.")

