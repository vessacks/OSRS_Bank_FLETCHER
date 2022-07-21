#powerminer 2.0.0
#note: needs breakRoller and clickableEntity

from calendar import c
import pyautogui
import time
import numpy as np
from pyHM import mouse

import breakRoller
import clickableEntity

#notes:
#1 start with knife and full logs
#2 bank set to dep/withdraw all
#3 outside bank when start


#gets the coords for everything
#decent parameters are (2,10) for slots and (5,30) for rocks on samsung monitor
#decent parameters are (7,300) for slots and unknown for rocks on samsumg monitor

inv_log_bow = clickableEntity.clickableEntity(2,10)
print("we will now take coords for inventory log/bow" )
inv_log_bow.getcoords()

inv_knife = clickableEntity.clickableEntity(2,10)
print("we will now take coords for inventory knife" )
inv_knife.getcoords()

bank_entrance = clickableEntity.clickableEntity(5,30)
print("we will now take coords for bank entrance")
bank_entrance.getcoords()

bank_log = clickableEntity.clickableEntity(2,10)
print("we will now take coords for bank log" )



bank_log.getcoords()

bank_exit = clickableEntity.clickableEntity(2,4) #these coords are a guess, and a bad one at that
print("we will now take coords for bank exit" )
bank_exit.getcoords()

ready = input('Ready?')

#this determines how long to run for
count = 0
startTime = time.time()

countOrSecond = input('would you like to run for #seconds or #counts? (s/c)')
if countOrSecond == 's':
    durationSeconds = float(input('please input number of seconds to run (1h= 3600, 6h=21600'))
    
elif countOrSecond == 'c':
    durationCount = int(input('please enter the number of counts to perform'))
    
else:
    print('you\'ve messed something up, quitting program now' )

 

def normdistwait(mean, standarddev):
    #normal distribution determines how long to wait between rock clicks
    time.sleep(abs(np.random.normal(loc=mean,scale=standarddev)))
count = 0
startTime = time.time()

while True: #run loop 
    inv_knife.genclick()
    normdistwait(.6,.1)
    inv_log_bow.genclick()
    normdistwait(1.1,.1)
    pyautogui.keyDown('space')
    normdistwait(.15,.03)
    pyautogui.keyUp('space')
    normdistwait(47,.7)
    bank_entrance.genclick()
    normdistwait(1.2,.07)
    inv_log_bow.genclick()
    normdistwait(.6,.07)
    bank_log.genclick()
    normdistwait(.6,.07)
    bank_exit.genclick()
    normdistwait(.6,.07)
   
    #breakroller
    #breakRoller.breaktime()

    #this is the count/seconds section
    count += 1
    runTime = round(time.time() - startTime,0)
    countSec = round(count/runTime,2)
    print('count = %s | runTime = %s seconds | count/sec = %s '%(count, runTime, countSec))

    #termination conditions
    if pyautogui.position() == pyautogui.Point(0,0):
        print('quitting program')
        quit()
    if countOrSecond == 's' and runTime > durationSeconds:
        print('quitting program')
        quit()
    if countOrSecond == 'c' and count > durationCount:
        print('quitting program')
        quit()
    


