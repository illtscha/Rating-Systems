import random
from plot import plot
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
    zufall = random.uniform(1, gesamt)
    if zufall <= skill[player1]:
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

def rating_update():
    with open('ratings.json', 'r') as data:
        js = data.readline()
        ratings = json.loads(js)
    return ratings

#while(True):
for l in range(1000):

    n_gesamt = len(skill)#anzahl der personen mit skill

    for i in skill: #für person in liste von personen mit skill

        temp = list(ratings.items())
        res = [idx for idx, key in enumerate(temp) if key[0] == i]
        print(res[0])
        for a in range(n_gesamt - res[0] - 1):#für jede person die noch nicht gegen i gekämpft hat

            #print(i,key_list[val_list.index(n+a)])#kampf ausgeben
            winner = fight(i, key_list[0+1])#kampf ausführen

            if winner == i:#wenn i gewonnen hat
                looser = key_list[0+1]#dann ist der verlierer der andere
            elif winner == key_list[0+1]:#wenn der andere gewonnen hat
                looser = i#dann ist der verlierer i


            point_update(winner, looser)#punkte updaten

            with open('log.txt', 'a') as f:#log schreiben
                f.write("\nWinner: %s %s +1 Looser: %s %s -1"%(winner,ratings[winner],looser,ratings[looser]))#log schreiben

        ratings = rating_update()#ratings updaten

        with open('log.json', 'r') as data:#log schreiben
            js = data.readline()#log schreiben
            log = json.loads(js)#   log schreiben
        print(ratings)#log schreiben
        log[i].append(ratings[i])#log schreiben
        with open('log.json', 'w') as ratings_file:#    log schreiben
            ratings_file.write(json.dumps(log))#log schreiben

    print(l)
plot()


