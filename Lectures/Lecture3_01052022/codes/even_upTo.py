num = int(input("Enter a number greater than or equal to 2: "))

if(num < 2):
    print("Bad Input")
else:
    i = 2
    while(i <= num):
        print(i)
        i += 2

