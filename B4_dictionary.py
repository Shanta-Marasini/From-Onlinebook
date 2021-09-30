print('hello shiva baba my world')

bday = {
    "Shiva": 'april 1',
    'Hari' : 'april 3',
    'Shyam' : 'april 4',
    'Shraddha' : 'april 5'
}

# keys
# for i in bday:
#     print(i)
#
# for i in bday.keys():
#     print(i)
#
# print(bday.keys())
# print(list(bday.keys()))

#values
# for i in bday.values():
#     print(i)
#
# for i in bday:
#     print(bday[i])
#
# print(bday.values())
# print(list(bday.values()))

#key-value pairs
# for i in bday.items():
#     print(i)
# print('')
#
# for i in bday.items():
#     print(list(i))
# print('')
#
# for i,j in bday.items():
#     print(i,j)
#
# print(bday.items())
# print('')
# print(bday)

#accessing
# print('Shiva' in bday)
# print('Shiva' in bday.keys())
#
# print('april 1' in bday)  # not true
# print('april 1' in bday.values())

#get method no error generating
print(bday.get('Shiva', 'none'))
print(bday.get('Shiv', 'none'))

#Set default
bday.setdefault('Baba','April 1')
bday.setdefault('Shiva','August 1')

print(bday)
