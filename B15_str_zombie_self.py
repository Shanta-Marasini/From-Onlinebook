import random,sys
print('Hello Shiva baba my world')

dice = ['shotgun','brain']

def rollDice(points):
    print('------')
    pointsFun = points
    while True:
        x = random.choice(dice)
        y = random.choice(dice)
        z = random.choice(dice)
        resultDice = [x,y,z]
        print('The dice is rolled,result is: ')
        print(resultDice)
        if resultDice.count('shotgun') == 3:
            print('You got all shotguns so you lose')
            break
        else:
            thisTimeBrain = resultDice.count('brain')
            pointsFun = pointsFun + thisTimeBrain
            print(f'You got {thisTimeBrain} brains.So Score = {pointsFun}')
            if pointsFun >= 13:
                print('You got 13 brains.You may win lets give a chance to next player')
                break
            answer = input('would you like to reroll? (y/n):')
            if answer == 'n':
                break

    return pointsFun


def whoWin(score):
    return score >= 13


print('This is zombie dice game:')

while True:
    totalScore1 = 0
    totalScore2 = 0
    while True:
        print('Player 1')
        print('Lets roll your dice:')
        totalScore1 += rollDice(totalScore1)
        print(f'1 : {totalScore1}')

        print('Player 2')
        print('Lets roll your dice:')
        totalScore2 += rollDice(totalScore2)
        print(f'2 : {totalScore2}')

        print('--------------------------')
        print('--------------------------')

        if totalScore1 >= 13 or totalScore2 >= 13:
            break

        if totalScore1 == 0 and totalScore2 == 0:
            break


    if whoWin(totalScore1) == whoWin(totalScore2):
        print('tie have to replay')

    elif whoWin(totalScore1):
        print('player 1 won')
        sys.exit()

    elif whoWin(totalScore2):
        print('player 2 won')
        sys.exit()









