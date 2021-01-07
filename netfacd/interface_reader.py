#!/usr/bin/env python3

import netifaces
print(netifaces.interfaces())


print(netifaces.interfaces())

for i in netifaces.interfaces():

    print('\n**************Details of Interface - ' + i + ' *********************')
      # print(netifaces.ifaddresses(i))
    try:
      # print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK])
        print('MAC: ',end='')
    
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print('IP: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message
