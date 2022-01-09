num = int(input("Enter a number between 1 and 10: "))

if(num < 1 and num > 10):
    print("Bad Input!")
else:
    i = 0
    while(i < num):
        print("*"*i)
        i += 1
