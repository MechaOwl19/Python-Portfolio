import random

player = input ('r for rock, p for paper, s for scissors')
computer = random.choice(['r','p','s'])

if (player == 'r' and computer == 's') or (player == 's' and computer == 'p' ) or (player == 'p' and computer == 'r'):
    print('you won')

elif (player == 's' and computer == 'r') or (player == 'p' and computer == 's' ) or (player == 'r' and computer == 'p'):
    print('you lost')

elif player == computer:
    print('tie')
    