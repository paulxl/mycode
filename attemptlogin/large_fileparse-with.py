#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginNotFail = 0

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            print(line.split(" ")[-1])
            loginfail += 1 # this is the same as loginfail = loginfail + 1

print("The number of failed log in attempts is", loginfail)

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile2:

    # loop over the file
    for line2 in kfile2:
        # if this 'fail pattern' appears in the line...
        if " -] Authorization failed" in line2:
            loginNotFail += 1 # this is the same as loginfail = loginfail + 1

print("The number of successfull log in attempts is",  loginNotFail)


