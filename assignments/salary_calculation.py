hours = eval(input("Enter the number of hours worked: "))
rate = eval(input("Enter the hourly rate: "))

print("You have earned", 
    (str(hours*rate))*(hours<=40), 
    (str(40*rate + (hours-40)*rate*1.5))*(hours>40),
    "dollars" )