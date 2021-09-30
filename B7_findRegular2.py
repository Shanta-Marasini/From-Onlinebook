import re
print('hello Shiva baba my world')

#zero or multiple expressions
so = re.compile(r'bat(wo)*man')
mo = so.search('I am a batman')
mo2 = so.search('I am a batwoman')
mo3 = so.search('I am a batwowowowowoman')
print(mo.group())
print(mo2.group())
print(mo3.group())
print()

#one or multiple expressions
soo = re.compile(r'bat(wo)+man')
moo = soo.search('I am a batman')
moo2 = soo.search('I am a batwoman')
moo3 = soo.search('I am a batwowowowowoman')
print(moo==None)
print(moo2.group())
print(moo3.group())
print()

#match multiple with braces
seo = re.compile(r'(go){3}')
meo = seo.search('gogogo')
print(meo.group())
meoo = seo.search('go')
print(meoo==None)

seoo = re.compile(r'(go){3,5}')
meoo = seoo.search('gogogo gogogogo')
print(meoo.group())
seoo1 = re.compile(r'(go){,5}')
seoo2 = re.compile(r'(go){3,}')
print()

#Greedy and non-greedy matching
fo = re.compile(r'(ha){3,5}')
go = fo.search('hahahahaha hahaha haha')
print(go.group())
foo = re.compile(r'(ha){3,5}?')
goo = foo.search('haha hahaha hahahaha')
print(goo.group())
