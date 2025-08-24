import datetime

import time

def list():
    time.sleep(0.5)
    print("| Note | For multiple dishes type the code for the dishes in the order with a space between them |")
    time.sleep(0.5)
    print("|P|izza | Rs. 100")
    time.sleep(0.5)
    print("|B|urger | Rs. 50")
    time.sleep(0.5)
    print("|Pa|sta | Rs. 60")
    time.sleep(0.5)

def error():
    print("| Error | Invalid Operation |")

def thankyou():
    print("| Thank you for Shopping |")

def repeat0():
    global repeat
    time.sleep(0.5)
    repeat = input("|O|rder again || |N|o and exit: ")
    if repeat == "O" or repeat == "o":
        repeat = True
    elif repeat == "N" or repeat == "n":
        time.sleep(0.5)
        thankyou()
        repeat = False
    else:
        time.sleep(0.5)
        error()

def work(price0, dish):
    time.sleep(0.5)
    ask0qu = int(input("Quantity: "))
    ask0pr = ask0qu * price0
    time.sleep(0.5)
    print("Dish:" + dish + "| Quantity:",ask0qu,"| Price:",ask0pr,"| Time:",datetime.datetime.now())
    repeat0()

def work1(dish1,dish2,price1,price2):
    time.sleep(0.5)
    ask0qu = int(input("Quantity of " + dish1 + ": "))
    time.sleep(0.5)
    ask0qu1 = int(input("Quantity of " + dish2 + ": "))
    ask0pr = (ask0qu * price1) + (ask0qu1 * price2)
    time.sleep(0.5)
    print("Dish:" + dish1 + "," + dish2 + "| Quantity:",ask0qu,",",ask0qu1,"| Price:",ask0pr,"| Time:",datetime.datetime.now())
    repeat0()

def work2(dish1,dish2,dish3,price1,price2,price3):
    time.sleep(0.5)
    ask0qu = int(input("Quantity of " + dish1 + ": "))
    time.sleep(0.5)
    ask0qu1 = int(input("Quantity of " + dish2 + ": "))
    time.sleep(0.5)
    ask0qu2 = int(input("Quantity of " + dish3 + ": "))
    ask0pr = (ask0qu * price1) + (ask0qu1 * price2) + (ask0qu2 * price3)
    time.sleep(0.5)
    print("Dish:" + dish1 + "," + dish2 + "," + dish3 + "| Quantity:",ask0qu,",",ask0qu1,",",ask0qu2,"| Price:",ask0pr,"| Time:",datetime.datetime.now())
    repeat0()

repeat = True
while repeat == True:
    try:
        time.sleep(0.5)
        print("| Welcome to coders cafe | Fast Catering Inc. |")
        time.sleep(0.5)
        menu = input("Type |M| to view menu: ")
        if menu == "M" or menu == "m":
            list()
            ask0 = input("Choose the dish: ")
            if ask0 == "P" or ask0 == "p":
                work(price0 = 100, dish = "Pizza")

            elif ask0 == "b" or ask0 == "B":
                work(price0 = 50, dish = "Burger")

            elif ask0 == "Pa" or ask0 == "pa":
                work(price0 = 60, dish = "Pasta")

            elif ask0 == "P B" or ask0 == "P b" or ask0 == "p B" or ask0 == "p b":
                work1(dish1 = "Pizza", dish2 = "Burger", price1 = 100, price2 = 50)

            elif ask0 == "P Pa" or ask0 == "P pa" or ask0 == "p Pa" or ask0 == "p pa":
                work1(dish1 = "Pizza", dish2 = "Pasta", price1 = 100, price2 = 60)

            elif ask0 == "B Pa" or ask0 == "B pa" or ask0 == "b Pa" or ask0 == "b pa":
                work1(dish1 = "Burger", dish2 = "Pasta", price1 = 50, price2 = 60)

            elif ask0 == "P B Pa" or ask0 == "p b pa" or ask0 == "P b pa" or ask0 == "P B pa" or ask0 == "P b Pa" or ask0 == "p B pa" or ask0 == "p B Pa" or ask0 == "p b Pa":
                work2(dish1 = "Pizza", dish2 = "Burger", dish3 = "Pasta",price1 = 100,price2 = 50, price3 = 60)
            else:
                error()
                repeat0()
        else:
            error()
            repeat0()
    except:
        error()
        repeat0()
