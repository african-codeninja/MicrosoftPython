# to get current date and time we need to use the datetime librabry
from datetime import datetime, timedelta
# The now function return current date and time as a datetime object

today = datetime.now()

print('Today is: ' + str(today))
# You must convert the datetime object to a string
# this is before you can concatenate it to another string
print('')
print('Getting dates using a day as our baseline')
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))
print('')
print('Getting dates using a week as our baseline')
one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was: ' + str(last_week))