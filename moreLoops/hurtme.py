#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for x in farms:
    if x["name"] == "NE Farm":
        print(x.values())

print("\n\n")

print("if you want to see what is on ")
while True:
    userInput1 = input("'NE Farm', input 1: for 'W Farm', input 2: for 'SE Farm', input 3  ").strip()

    if userInput1 == "1":
        for y in farms:
            if y["name"] == "NE Farm":
                print(y.values())
        break

    elif userInput1 == "2":
        for w in farms:
            if w["name"] == "W Farm":
                print(w.values())
        break

    elif userInput1 == "3":
        for z in farms:
            if z["name"] == "SE Farm":
                print(z.values())
        break

#elif userInput1 != "1" or userInput1 !="2" or userInput !="3":
    else:
        print("only 1,2,3 acceptable inputs, try again")



