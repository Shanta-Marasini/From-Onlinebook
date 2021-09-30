print('Hello Shiva baba my world')

print('Enter the sentence to tale to the pig latin:')
message = input()
VOWELS = ('a','e','i','o','u','y')

piglatin= []
#split and work on each word at one for loop
for sword in message.split():
    #separate non letters at the start of the word
    prefixNonLetters = ''
    while len(sword)>0 and not sword[0].isalpha():  #if not alphabet
        prefixNonLetters+=sword[0]
        sword=sword[1:]
    if len(sword) == 0:
        piglatin.append(prefixNonLetters)
        continue

    suffixNonLetters =''
    while not sword[-1].isalpha():
        suffixNonLetters += sword[-1]
        sword = sword[:-1]


    wasUpper=sword.isupper()
    wasTitle =sword.istitle()

    sword=sword.lower()
    #if prefixa is consonant
    prefixConsonant=''
    while len(sword) > 0 and not sword[0] in VOWELS:
        prefixConsonant += sword[0]
        sword = sword[1:]

    if prefixConsonant !='':
        sword+= prefixConsonant + 'ay'
    else:
        sword += 'yay'

        # Set the word back to uppercase or title case:
    if wasUpper:
        sword = sword.upper()
    if wasTitle:
        sword = sword.title()

    # Add the non-letters back to the start or end of the word.
    piglatin.append(prefixNonLetters + sword + suffixNonLetters)


print(' '.join(piglatin))