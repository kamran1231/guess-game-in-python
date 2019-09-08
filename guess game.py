
print('welcome to my guess game:')

print('you have only 9 turn if you dont guess within 9 you will lost this game')

n = 18
x = int(input('enter your guess number: '))

no_of_guess = 9
while True:
    no_of_guess -= 1
    if no_of_guess < 1:
        print('your turn over: \n GAME OVER \n YOU LOST')


    elif x > 18:
        print('your number is larger than guess number so input small number \n number of guess left:',no_of_guess)
        x = int(input('enter your guess number: '))

    elif x < 18:
        print('your number is smaller than guess number so input big number \n number of guess left:',no_of_guess)
        x = int(input('enter your guess number: '))
    else:
        print('congratulation you won this battel',no_of_guess)
        break