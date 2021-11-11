'''
@title: exercise6
@author: habi2
@date: 24/10/2021

Create a dictionary with keys the names of the months of the year and values the number of
days of that month (‘January’: 31, etc). Create another dictionary with keys: day, month,
year and leapYear. Ask the user to fill the second dictionary. The value of leap year must be
automatically set. The value of the month and day must be correct taking into account leap
years (those years February has 29 days). If any value is not correct we will ask the user until a
correct value is entered. Print the date with format: March 23, 2019, non-leap year
'''

months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31,
'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31,
'November': 30, 'December': 31}

day_input = int(input('Enter the day: '))
month_input = str(input('Enter the month (in minus): ').capitalize())
year_input = int(input('Enter the year: '))

a = 0
b = months.get(month_input)
while a == 0:
    if day_input == 29 and month_input == 'February' and year_input % 4 == 0:
        print(f'February 29, {year_input}, leap year')
        a = 1
    elif (month_input in months) == True and day_input < months[month_input] and day_input > 1:
        a = 1
    else:
        while (month_input in months) != True or day_input > months[month_input] or day_input < 1:
            day_input = int(input('Enter the day: '))
            month_input = input('Enter the month (in minus): ').capitalize()
            year_input = int(input('Enter the year: '))
        

the_other_dic = {'day': day_input, 
'month': month_input,
'year': year_input,
'leapYear': ''}

if the_other_dic['year'] % 4 == 0:
    the_other_dic['leapYear'] = 'leap year'
else:
    the_other_dic['leapYear'] = 'non-leap year'

print('%s %i, %i, %s'%(the_other_dic['month'], the_other_dic['day'], the_other_dic['year'], the_other_dic['leapYear']))