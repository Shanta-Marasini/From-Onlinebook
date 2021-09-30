import random
print('hello Shiva baba my world')

#taking list input from user
def lToString(listname):
    if len(listname) == 0:
        print('oops list is empty')
    else:
        for i in range(len(listname)):
            if i == (len(listname)-1):
                print(" and " + str(listname[i]) + "\'" )
            elif i == len(listname)-2:
                if i == 0:
                    print("\'" + str(listname[i]) , end='')
                else:
                    print(str(listname[i]),end='' )
            elif i == 0:
                print("\'" + str(listname[i]) + ', ', end='')
            else:
                print(str(listname[i]) + ", " ,end='')


listt=[]

print('Enter no of elements of list: ',end='')
n = int(input())
if n != 0:
    print("Now enter "+ str(n) + " elements")

for i in range(n):
    element = input()
    listt.append(element)


lToString(listt)


