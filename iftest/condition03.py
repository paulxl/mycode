#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("Hostname matches expected config")


if hostname == "mtg":
    print("Testing to see if this hits just on lowercase not modified ....")

if hostname == "MTG":
    print("Another test for all caps.......") 

## Always print out to the user
print("Exiting the script")



