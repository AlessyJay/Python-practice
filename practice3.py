width = eval(input("Width: "))
length = eval(input("Length: "))
area = width*length
sqrA = min(width, length)
sqrB = min(width, length)
square = sqrA*sqrB
solution = area/square

if width < 0 and length < 0:
    print("It can't be negative!")
elif width > 0 and length < 0:
    print("Length should not be negative!")
elif width < 0 and length > 0:
    print("Width can't be negative!")
else:
    print("They require ", int(solution), "square/2 to define a minimum square.")

