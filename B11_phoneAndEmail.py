import  pyperclip,re
# print('hello Shiva baba my world')

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   # area code
    (\s|-|\.)?           #separator
    (\d{3})              #1st three digits
    (\s|-|\.)             #separator
    (\d{4})                #last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
     )''',re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-z0-9._%+-]+        #uername
    @                          #@symbol
    [a-zA-Z0-9.-]+                #domainame
    (\.[a-zA-Z]{2,4})                  #dot-something
    )''',re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches =[]
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8]!= '':
        phoneNum += 'x'+ groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')



#
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?                # area code
#     (\s|-|\.)?                        # separator
#     (\d{3})                           # first 3 digits
#     (\s|-|\.)                         # separator
#     (\d{4})                           # last 4 digits
#     (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
#     )''', re.VERBOSE)
#
# emailRegex = re.compile(r'''(
#     [a-zA-Z0-9._%+-]+      # username
#     @                      # @ symbol
#     [a-zA-Z0-9.-]+         # domain name
#     (\.[a-zA-Z]{2,4})       # dot-something
#     )''', re.VERBOSE)
#
# # Find matches in clipboard text.
# text = str(pyperclip.paste())
#
# matches = []
# for groups in phoneRegex.findall(text):
#     phoneNum = '-'.join([groups[1], groups[3], groups[5]])
#     if groups[8] != '':
#         phoneNum += ' x' + groups[8]
#     matches.append(phoneNum)
# for groups in emailRegex.findall(text):
#     matches.append(groups[0])
#
#
# #Copy results to the clipboard.
# if len(matches) > 0:
#     pyperclip.copy('\n'.join(matches))
#     print('Copied to clipboard:')
#     print('\n'.join(matches))
# else:
#     print('No phone numbers or email addresses found.')
