name = input('What is your name?: ')
age = int(input('What is your age?: '))
income = float(input('What is your income?: '))

#Display the data.
print('Here is the data you enterated: ')
print('Name: ',name)
print('Age: ',age)
print('Income: ', format(income, '12,.2f'))