#!/usr/bin/env python3

print("We are giving away a trip.")
print("need some info to determine what trip you are best suited for.")

while True:
    kids = input("Do you have children? Y or N").strip().lower()

    if kids == "y":
        takeKids()
        break

    elif kids =="n":
        travelFreedom()
        break

    else: 
        print("You don't know if you have kids?")
        lastOption()

def takeKids(): 
    while True:
        kidsTake = input("Do you plan to take them with you? Enter Y or N").strip().lower()

        if kidsTake == "y":
            takingKids()
            break

        elif kidsTake == "n":
            travelFreedom()
            break

        else:
            print("So you can't answer simple questions. ")
            lastOption()



def lastOption():
    print("Since you can't answer simple questions:")
    print("We are going to send you to Disney World in LA")
    print("on the busiest day available.... Enjoy the tourist...")

def takingKids():
    while True:
        kidsAbroad = input('Are you willing to travel abroad with the kids? Y or N').strip().lower

        if kidsAbroad == "n":
            noKidsAbroad()
            break

        elif kidsAbroad == "y":
            print("Your going to Europe to visit Castels")
            break

        else :
            print("tough question and can't answer correctly, then")
            lastOption()

def noKidsAbroad():
    while True:
        seaSickKids = input("Does anybody in the family get sea sick? Y or N").strip().lower

        if seaSickKids == "y":
            print("You get a National Parks Pass and an RV rental")
            break
        elif seaSickKids == "n":
            print("You just won a Carnaval Trip in the Bahamas")
            break
        else:
            print("You don't know?.....")
            lastOption()

# def kidsAbroad():
 #   castels = input("Your going to Europe to visit Castels")
def travelFreedom():
    while True:
        abroadY = input("Do you want to travel overseas?  Y or N").strip().lower()

        if abroadY == "y":
            abroad1()
            break
        elif abroadY == "n":
            noAbroad()
            break
        else :
            lastOption()

def abroad1():
    while True:
        drink = input("Do you like wine?  Y or N").strip().lower()

        if drink == "y":
            print("Sending you to Europe to go wine tasteing.  Enjoy")
            break
        elif drink =="n":
            print("You're going to the Orient to discover new cultures")
            break
        else:
            lastOption()
        
print("Bon Voyage")
