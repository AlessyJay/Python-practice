def first():
    #เขียนโปรแกรมรับ input 1 ตัวและตรวจสอบว่าจำนวนนั้นเป็นเลขคู่หรือคี่

    while True:
        ans = eval(input("Number: "))
        if ans % 2 == 0:
            print("Even")
        else:
            print("Odd")

def second():
    #เขียนโปรแกรมที่รับ input เป็นจำนวนเต็มและตรวจสอบว่ามีค่ามากกว่า 0 หรือไม่

    while True:
        ans = eval(input("Number: "))

        if ans > 0:
            print("More than 0")
        else:
            print("Less than 0")

def third():
    #เขียนโปรแกรมรับ input 1 ตัวและตรวจสอบว่ามากกว่า น้อยกว่า หรือเท่ากับ 0
    
    while True:
        ans = eval(input("Number: "))

        if ans == 0:
            print("Your number is equal to 0")
        elif ans > 0:
            print("Your number is more than 0")
        else:
            print("Your number is less than 0")

def fourth():
    #เขียนโปรแกรมรับ input 1 ตัวและตรวจสอบว่ามีค่ามากว่า 0 หรือไม่และเป็น odd หรือ even

    while True:
        ans = eval(input("Number: "))

        if ans < 0:
            if ans % 2 == 0:
                print("Negative even")
            else:
                print("Negative odd")
        elif ans > 0:
            if ans % 2 == 0:
                print("Positive even")
            else:
                print("Positive odd")
        elif ans == 0:
            print("Equal to 0")

def fifth():
    #เขียนโปรแกรมรับ input 2 ตัวออกมาและให้พื้นที่สี่เหลี่ยมโดยที่จำนวนเต็มต้องไม่ต่ำกว่าหรือเท่ากับ 0

    while True:
        length = eval(input("Length: "))
        width = eval(input("Wdith: "))

        if length <= 0 and width <= 0:
            print("Please, put positive numbers or more than 0!!")
        elif length < 0 and width > 0:
            print("Your length is less than 0, please make it more than 0!")
        elif length > 0 and width < 0:
            print("Your width is less than 0, please make it more than 0!")
        elif length > 0 and width > 0:
            sqrt = length * width
            print("Your shape is: ", sqrt)

def sixth():
    #เขียนโปรแกรมรับ input 1 ตัวเป็นจำนวนเต็มปีค.ศ.และให้ตรวจสอบเทียบกับปีพศ

    while True:
        AD = eval(input("AD: "))
        BY = AD +543
    
        if AD >= 0:
            print("Buddha's Year: ", BY)
        else:
            print("Please, make sure that you put positive numbers!")

def seventh():
    #เขียนโปรแกรมรับ input 1 ตัวออกมาเป็นค่า Fahrenheit และเปลี่ยนเป็น Celsius

    ans = input("Please, select your degree (F/C): ").upper()

    if ans == "F":
        while True:
            F = eval(input("Fahrenheit: "))
            C = 5 * (F - 32) / 9
            if F >= 32:
                print("celsius: ", C)
            else:
                print("Too cold to live!")
        
    elif ans == "C":
        while True:
            C = eval(input("Celsius: "))
            F = (C * 9/5) + 32
            if C >= 0:
                print("Fahrenheit: ", F)
            else: 
                print("Too cold to live!")


def eight():
    

print(seventh())