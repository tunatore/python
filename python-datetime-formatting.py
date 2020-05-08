# Created on Jul 25, 2013

# @author: tunatore

import time
import calendar
from datetime import date

currenTimeTuple = time.localtime(time.time())
print("current timeTuple :", currenTimeTuple)

# accessing tuple values
print("current year:", currenTimeTuple[0])
print("current month:", currenTimeTuple[1])
print("current day:", currenTimeTuple[2])

print("current hour:", currenTimeTuple[3])
print("current minute:", currenTimeTuple[4])
print("current second:", currenTimeTuple[5])

print("\n")
# getting calendar
calenderTxt = calendar.month(2013, 7)
print(calenderTxt)

# formatted times
print(time.asctime(currenTimeTuple))
print(time.strftime("%Y-%m-%d %H:%M:%S", currenTimeTuple))
print(time.strftime("%d-%m-%Y %H:%M:%S", currenTimeTuple))

# current date formatted
nowDate = date.fromtimestamp(time.time())

# ISO format current
print("Now", nowDate.isoformat())
print("Now Custom Format", nowDate.strftime("%d/%m/%y"))
