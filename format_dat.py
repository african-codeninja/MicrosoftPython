# to get current date and time we need to use the datetime librabry
from datetime import datetime

# The now function return current date and time as a datetime object

today = datetime.now()

# use, day, month, year, hour, minute, second functions to display only part of the date
# all these functions return intergers
#convert them to strings before concatenating them to another string
print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))
print('Week: ' + str(today.weekday))