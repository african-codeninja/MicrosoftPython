# to get current date and time we need to use the datetime librabry
from datetime import datetime, timedelta

#ask user to input birthday
birthday = input('when is your birthday (dd/mm/yyyy)?  ')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print('Birthday: ' + str(birthday_date))

one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))
