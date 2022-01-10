def leap_calc(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 'Leap year!'
            else:
                return 'Not a leap year!'
        else:
            return 'Leap year!'
    else:
        return 'Not a leap year!'

user_year = int(input('Enter a year: '))
print(leap_calc(user_year))
