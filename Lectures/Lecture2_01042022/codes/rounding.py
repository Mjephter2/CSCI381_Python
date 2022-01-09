num1 = 34.56
num2 = 34.48

# without built-in round()
print(num1, "->", (num1+0.5)//1.0)
print(num2, "->", (num2+0.5)//1.0)

# with built-in round()
print(num1, "->", round(num1))
print(num2, "->", round(num2))