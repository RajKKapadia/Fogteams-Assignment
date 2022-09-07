import re

# Read the data file
with open('training_data.txt', 'r') as file:
    lines = file.readlines()

heroes_info = {}

# Loop over all the training data
for line in lines:
    
    game_data = line.strip().split(',')
    winner = int(game_data[-1])
    
    if winner == 1:
        for i, hero in enumerate(game_data[:-1]):
            hero = re.sub(r'[^a-zA-Z]', ' ', hero)
            # if hero key not in heroes_info create it with empty data
            if hero not in heroes_info:
                heroes_info[hero] = {
                    'played': 0,
                    'won': 0,
                    'lost': 0
                }
            
            # for the first five heroes
            if i // 5 == 0:
                heroes_info[hero]['played'] += 1
                heroes_info[hero]['won'] += 1
            else:
                heroes_info[hero]['played'] += 1
                heroes_info[hero]['lost'] += 1
    else:
        for i, hero in enumerate(game_data[:-1]):
            # if hero key not in heroes_info create it with empty data
            if hero not in heroes_info:
                heroes_info[hero] = {
                    'played': 0,
                    'won': 0,
                    'lost': 0
                }
            
            # for the first five heroes
            if i // 5 == 1:
                heroes_info[hero]['played'] += 1
                heroes_info[hero]['won'] += 1
            else:
                heroes_info[hero]['played'] += 1
                heroes_info[hero]['lost'] += 1

for hero, data in heroes_info.items():
    heroes_info[hero]['win_percentage'] = round(data['won']/data['played'], 4)

# Read the input
N = int(input())
for _ in range(N):
    line = input().strip().split(',')
    t1 = line[:5]
    t2 = line[5:]

    p1 = 0
    for h in t1:
        p1 += heroes_info[h]['win_percentage']
    
    p2 = 0
    for h in t2:
        p2 += heroes_info[h]['win_percentage']

    if p1 > p2:
        print(1)
    else:
        print(2)
