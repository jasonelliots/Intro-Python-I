"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month of the current year. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.


Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

entered_args = sys.argv

currentMonth = datetime.now().month
currentYear = datetime.now().year

print(currentMonth)
print(currentYear)
# print(entered_args)

def cal(*args):
  newargs = args[0]
  print(newargs) 
  if len(newargs) == 1:
    # user passed in no args, print calendar for the currenty month of the current year
    print(calendar.month(currentYear, currentMonth))
  elif len(newargs) == 2: 
    # user passed in 1 arg, print calendar for that month (the arg passed) of the current year
    print(calendar.month(currentYear, int(newargs[1])))
  elif len(newargs) == 3:
    # user passed in 2 args, print calendar for that month (first arg) and that year (second arg)
    print(calendar.month(int(newargs[2]), int(newargs[1])))
  else:
    print("Please enter month and year")

cal(entered_args)

  

