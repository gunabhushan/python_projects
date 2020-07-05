from random import randint
from sys import argv
answer = randint(1,10)


while True:
    try:
        print(answer)
        guess = input('guess a number 1 to 10:  ')
        if int(guess)>0 and int(guess)<11:
            if int(guess) == answer:
                print('you are a genius!')
                break
        else:
            print('hey bozo, I said 1 to 10')
    except ValueError:
        print('please enter a number')
        continue