# 1. print two strings 
# 2. you escape sequences to print "" , new line, tab 
# 3. concatenate both stings
# 4. use len() to find length of new string
# 5. print type() of new string
# 6. format the string; combine string and int types 


str1 = "Hello, how are you?"
str2 = 'I\'m good!'
age = 21
location = 'California'
name = 'KV'

print('string 1 is : ' + str1)
print('string 2 is : ' + str2)
print('==========================')

print('\tstring 1 is : ' + str1)
print('\nstring 2 is : ' + str2)
print('==========================')

str3 = str1 + ' ' + str2
print(str3)
print('==========================')

print('This string\'s length is:' + str(len(str3)))
print('==========================')

print(type(str3))
print('==========================')

print(f'My age is {age} and I am from {location}!')
print('==========================')