dollar_amount = eval(input("Enter some amount of money: "))
centAmount = dollar_amount * 100

num_halfDollar = centAmount//50
centAmount %= 50

num_quarters = centAmount//25
centAmount %= 25

num_dimes = centAmount//10
centAmount %= 10

num_nickels = centAmount//5
centAmount %= 5

print("Here's your change!")
print(num_halfDollar, "half-dollars")
print(num_quarters, "quarters")
print(num_dimes, "dimes")
print(num_nickels, "nickels")
print(centAmount, "pennies")

