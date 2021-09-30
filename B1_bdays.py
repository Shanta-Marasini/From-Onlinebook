print('hello Shiva baba my world')

#the one that stores friends birthday and also updates the database

bday = {
    'Shiva' : 'April 1',
    'Parvati' : 'May 1',
    'Bishnu' : 'June 1'
}

while True:
    print("write (q) to quit")
    print('Enter friends name:')
    fname = input()
    if fname == 'q':
        break
    if fname in bday:
        print(bday[fname] + ' is the bday of ' + fname)
    else:
        print('I dont have info for' + fname)
        print('so what is his birthday I can store it:')
        fbday = input()
        bday[fname]= fbday
        print('Birthday database is updated')