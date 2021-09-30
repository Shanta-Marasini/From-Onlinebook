import pprint
print('hello Shiva baba my world')

message = 'It was a bright cold day in April, and the clocks were striking\
thirteen.'
count = {}

for c in message:
    count.setdefault(c, 0)
    count[c] = count[c] + 1

print(count)
pprint.pprint(count)  #for sorted manner
print('')
#is equal to
print(pprint.pformat(count))
print()
pprint.pformat(count)