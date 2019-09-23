first_name = input('Please enter your Fisrt name: ')
last_name = input('please enter your last name: ')

output = 'Hello, '+ first_name + ' '+ last_name
print(output)
output = 'Hello, {} {}' .format(first_name, last_name)
print(output)
output = 'Hello, {1}, {0}' .format(first_name, last_name)
print(output)
#Only available in Python 3
output = f'Hello, {first_name} {last_name}'
print(output)