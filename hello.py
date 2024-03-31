# A programm that says hello, then ask for my name and age
print('What is your name? ')
myName = input()
print('Your name is ', myName)
print('The lenght of your name is', len(myName))

print('How old are you? ')
myAge = input()
print('You will be', str(int(myAge) + 1), 'in a year.')