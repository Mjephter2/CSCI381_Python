num = int(input("Enter a positive number: "))
if(num%10 == 0):
    print("Bad Input!")
    exit()

numCopy = int(num)
reverse = 0

print(num, " -> ", end="")
while numCopy > 0:
    reverse = reverse*10 + numCopy%10
    numCopy = numCopy//10
print(reverse)