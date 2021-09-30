print('Hello Shiva  baba my world')

def isPhoneNumber(text):
    if len(text) !=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return  False
    for i in range(4,7):
        if not text[i].isdecimal():
            return  False
    if text[7]!='-':
        return  False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print('is 444-222-3333 no:')
print(isPhoneNumber('444-222-3333'))
print('is hekkko hejjolo a no:')
print(isPhoneNumber('hekko jksdoojo'))

msg = 'You can call me at 333-333-3333 or also I\
 have next number 444-888-2323'

for i in range(len(msg)):
    chunk = msg[i:i+12]
    if isPhoneNumber(chunk):
        print('the no is :'+chunk)
print('done')