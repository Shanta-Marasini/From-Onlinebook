import re
print('Hello Shiva baba my world')

#Find phone number through regular expressions

#Which pattern to find
searchObject= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = searchObject.search('I hane a no 999-999-8383')
print( matchObject)
print(matchObject.group())
print(matchObject.groups())  #not grouped here
print()
so = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')   #gives two groups
mo = so.search('hello i am to be searched text: 993-334-3334')
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
print(mo)
print()

# if area code had parenthesis
soo= re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')  #two groups
moo = soo.search('i am for parenthesis (777)-443-3343')
print(moo.group())
areaCode, mainNo = moo.groups() #since it gives two tuples
print(areaCode)
print(mainNo)
print()

#pipe | character to find multiple expressions but returns only one
so0 = re.compile(r'bat|cat')
mo0 = so0.search('find bat or cat')
print(mo0.group())
print()

#more multiple words
so1 = re.compile(r'bat(man|can|phone)')
mo1 = so1.search('batphone is a batman')
print(mo1.group())
print(mo1.group(1))
print()

#optional part with ?
so2 = re.compile(r'bat(wo)?man')
mo2 = so2.search('I am batman')
print(mo2.group())
mo22 = so2.search('I am not a batwoman')
print(mo22.group())
print()
#Phone number with no code

so3 =re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo3 =so3.search('333-3333')
print(mo3.group())
mo33 = so3.search('343-232-4343')
print(mo33.group())