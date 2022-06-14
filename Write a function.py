def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0:
        return leap                 #this first code gives a wrong answer for the year (1992)
    else:
        return leap #(False)

year = int(input('Enter Year: '))
print(is_leap(year))

#####################################################################

def is_leap(year):
    leap = False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:                   #this one is the correct answer(passed all tests)
                return leap
        else:
            return True
    else:
        return leap

year = int(input())
print(is_leap(year))
