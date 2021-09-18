from random import randrange
n =randrange(1000)

while True:
    print('Welcome to Guess Game!\nGuess a number between 1-1000')
    inp=int(input('What number ?'))
    if inp == n:
        print(10*'-','\n|YOU WIN!|\n'+10*'-')
        break
    print('Input too Small \n' if (inp<n) else 'Input too Big\n' )
    print(10*'-')

    '''Source: Credit to https://www.youtube.com/watch?v=EBezqslQslc'''