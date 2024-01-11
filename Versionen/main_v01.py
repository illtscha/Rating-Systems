import random
import json

with open('stärke.json', 'r') as data:
    js = data.readline()
    skill = json.loads(js)
with open('ratings.json', 'r') as data:
    js = data.readline()
    ratings = json.loads(js)

key_list = list(skill.keys())
val_list = list(skill.values())

def fight(player1, player2):
    gesamt = skill[player1] + skill[player2]
    zufall = random.randint(1, gesamt)
    if zufall <= ratings[player1]:
        return player1
    else:
        return player2

def point_update(winner, looser):
    with open('ratings.json', 'r') as data:
        js = data.readline()
        pointsjs = json.loads(js)

    pointsjs[winner] = pointsjs[winner] + 1
    pointsjs[looser] = pointsjs[looser] - 1

    with open('ratings.json', 'w') as ratings_file:
        ratings_file.write(json.dumps(pointsjs))


while(True):
    with open('ratings.json', 'r') as data:
        js = data.readline()
        ratings = json.loads(js)
    n = 2
    n_gesamt = len(skill)

    for i in skill:

        #print(i)
        a = 1

        for a in range(n_gesamt - n + 1):

            print(i,key_list[val_list.index(n+a)])
            winner = fight(i, key_list[val_list.index(n+a)])
            if winner == i:
                looser = key_list[val_list.index(n+a)]
            elif winner == key_list[val_list.index(n+a)]:
                looser = i
            win = winner
            los = looser
            point_update(winner, looser)

            with open('log.txt', 'a') as f:
                f.write("\nWinner: %s %s +1 Looser: %s %s -1"%(win,ratings[win],los,ratings[los]))
        n+=1
    break

