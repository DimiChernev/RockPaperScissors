import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

pick = input('Choose [r]ock. [p]aper, or [s]cissors :)')

if pick == 'r':
    pick = rock
elif pick == 'p':
    pick = paper
elif pick == 's':
    pick = scissors
else:
    raise SystemExit('Invalid Input. Try again...')

pc_random = random.randint(1, 3)

pc_pick = ''

if pc_random == 1:
    pc_pick = rock
elif pc_random == 2:
    pc_pick = paper
else:
    pc_pick = scissors

print(f'The pc chose {pc_pick}.')

if (pick == rock and pc_pick == scissors) or \
        (pick == paper and pc_pick == rock) or \
        (pick == scissors and pc_pick == paper):
    print('You win!')
elif pick == pc_pick:
    print('Draw!')
else:
    print('You lose!')
