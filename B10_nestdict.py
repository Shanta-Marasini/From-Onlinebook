print('hello shiva baba my world')

allguests={
    'Bob':{
        'apple': 5,
        'banana' : 10
    },
    'Mary':{
            'apple': 5,
            'banana' : 10
        },
    'Brone':{
            'app': 5,
            'bana' : 10
        }
}

def noitems(guest,item):
    broughtno = 0
    for i,j in guest.items():
        broughtno = broughtno + j.get(item,0)
    return broughtno

print('Number of things being brought:')
print('apple:'+ str(noitems(allguests,'apple')))
print('banana:'+ str(noitems(allguests,'banana')))

# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
#              'Bob': {'ham sandwiches': 3, 'apples': 2},
#              'Carol': {'cups': 3, 'apple pies': 1}}
#
# def totalBrought(guests, item):
#     numBrought = 0
#     for k, v in guests.items():
#         numBrought = numBrought + v.get(item, 0)
#     return numBrought
#
# print('Number of things being brought:')
# print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
# print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
# print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
# print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
# print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

