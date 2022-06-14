def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0:
        return leap
    else:
        return leap #(False)

year = int(input('Enter Year: '))
print(is_leap(year))
