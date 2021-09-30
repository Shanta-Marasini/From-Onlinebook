print('Hello Shiva baba mly world')

#Putting strings inside other strings

# name = 'Shanta'
# age = 21
# print('My name is '+ name + '.I am '+ str(age) +' years old.')
# print('My name is %s.I am %s years old'%(name,age))
# print(f'My name is {name}.I am {age} years old.')
#
# print(name.isupper())
# print((name.upper()).isupper())
# print(name.isalpha())
# caste = 'human20'
# print(caste.isalnum())
# no = '8378'
# print(no.isdecimal())
# print(name.istitle())
# print(caste.istitle())
#
# #join list to string conversion
# listt= ['bat','ant','cat']
# print(','.join(listt))
# print(' '.join(listt))
# print('ABC'.join(listt))

#split string to list
# msg ='hi how can i help you'
# print(msg.split())
# print(msg.split('h'))

#justify strings
def justify(picnicitems,lwidth,rwidth):
    print('PICNIC ITEMS'.center(lwidth+rwidth,'-'))
    for i,j in picnicitems.items():
        print(i.ljust(lwidth,'.') + str(j).rjust(rwidth))


picitems = {
    'sandwich': 4,
    'Paratha' : 5,
    'hi' : 2
}
justify(picitems,20,4)

