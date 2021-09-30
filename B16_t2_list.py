print('hello shiva baba my world')

listt = [[1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
         [1,2,3,4,5,6],
         [1,2,3,4,5,6],
         [1,2,3,4,5,6],
         [1,2,3,4,5,6]]

# for row in listt:
#     for column in row:
#         print(column ,end='')
#     print()

for row in range(len(listt)):
    for column in range(len(listt[row])+2):
        print(listt[column][row] ,end='')

    print()

