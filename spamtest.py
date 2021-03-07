

myCat = {'size': 'fat', 'color': 'gray', 'discription': 'loud'}
myCat['size']
birthdays= {'hadal': '3.1', 'bob': '8.9', 'alice': '9.10', 'xiaonda': '4.8'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name]+ ' is the birthday of ' +name)
    else:
        print(' I do not have birthday information for ' + name)
        print('what is their birthday')


