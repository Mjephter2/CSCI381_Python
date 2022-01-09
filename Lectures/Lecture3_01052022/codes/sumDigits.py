# print all integers less than 1000 whose sum of digits is 20
for i in range(1000):
    # calculate sum of digits
    num = int(i)
    digSum = 0
    while(num > 0):
        digSum += num % 10
        num = num//10
    if digSum == 20:
        print(i)
