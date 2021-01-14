def addition():
    num1 = int(input("enter number  "))
    num2 = int(input("enter the number  "))
    num3 = num1 + num2
    print(" your final sum is %d" % (num3))


def multiplicalation():
    num4 = int(input("enter the number  "))
    num5 = int(input("enter the number  "))
    num6 = num4 + num5
    print(num6)


def division():
    num7 = int(input("enter num  "))
    num8 = int(input("enter num  "))
    num9 = num7 / num8
    print(num9)


def subtraction():
    num10 = int(input("enter the num "))
    num11 = int(input("enter the num"))
    num12 = num10 - num11
    print(num12)


def calculation():
    if record == 1:
        addition()
    elif record == 2:
        subtraction()
    elif record == 3:
        multiplicalation()
    elif record == 4:
        division()


def inputrecord():
    userinput = int(input(
        "what do you wnat to calculate  \n(1) Addition \n(2) Subtraction \n(3) Multiplication \n(4) Division \n(0) Cancel \n"))
    return (userinput)


while True:
    record = inputrecord()
    calculation()
    reply = input("Do You Want to calculate again (y/n)")
    record = inputrecord()
    calculation()

    if reply == "n" or record == 0:
        confirmcancel = input("are you sure(y/n)")
        if confirmcancel == "y":
            print("good bye ")
        break
