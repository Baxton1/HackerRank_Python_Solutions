#the leap year logic

1) the year can be evenly divided by 4, is a leap year

if (year % 4 == 0):
    leap = True

2) the year can be evenly divided by 100, it is NOT a leap year

if (year % 100 == 0):
    leap = False

3) the year is also evenly divisible by 400. Then it is a leap year.

if (year % 400 == 0):
    leap = True

So merging all this will be code for leap year

write your logic here
if (year % 4 == 0):
    leap = True
if (year % 100 == 0):
    leap = False
if (year % 400 == 0):
    leap = True
return leap

from the above we can conclude that a leap year which is divisible
by 4 but not or a year which is divisible by 400.

Write your logic here
if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    return leap
