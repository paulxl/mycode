#!/usr/bin/env python3

#star = "*"

countUp = 1
countDown=5

for x in range(5):
    print("*"*countUp)
    countUp +=1

for y in range(5,-1,1):
    print("*"*countDown)
    countDown -=1
