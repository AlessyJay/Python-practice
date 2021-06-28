Shopping = eval(input("Shopping: "))
Hour = eval(input("Hour: "))
Minute = eval(input("Minute: "))

h4 = ((Hour-4)*30)
h1 = ((Hour-1)*30)
m = 30

if Shopping >= 1000:
    if Hour <= 4:
        print("Your parking fee is free!")
    elif Hour > 4 and Minute/60 != 0:
        print("your parking fee is ", h4+m, "THB")
    elif Hour < 0 and Minute < 0:
        print("it can't be negative!")
elif Shopping < 1000:
    if Hour <= 1:
        print("Your parking fee is free!")
    elif Hour > 1 and Minute/60 != 0:
        print("Your parking fee is ", h1+m, "THB")
    elif Hour < 0 and Minute < 0:
        print("It can't bbe negative!")