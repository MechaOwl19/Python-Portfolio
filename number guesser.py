import random
def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'guess a number between 1 and {x}')) 
        if guess < random_num:
            print('too low')

        elif guess > random_num:
            print('too high')

    print ('OK you guessed it')


def guess_ai(x):
   
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':

        guess = random.randint(low, high)
        feedback = input (guess)

        if feedback == 'h':
            high = guess - 1

        elif feedback == 'l':
            low = guess + 1

    print('>:)')   


    
guess_ai(10000)
