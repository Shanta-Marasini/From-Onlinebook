import pyperclip
print('hello Shiva baba my world')

#add a star to along list

text=pyperclip.paste()
print(text)
#separate through new line

lines = text.split('\n')
print(lines)
for i in range(len(lines)):
    lines[i]= "*" + lines[i]
nexttext='\n'.join(lines)
pyperclip.copy(nexttext)