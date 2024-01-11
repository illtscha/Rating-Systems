import random
import simplejson as json
import matplotlib.pyplot as plt
import numpy as np
import ast
import math
from decimal import Decimal, getcontext

getcontext().prec = 10


with open('stärke.json', 'r') as data:
    js = data.readline()
    skill = json.loads(js)
rating = {}
for i in skill:
    rating[i] = 0
#print(lib.skill)
with open('ratings.json', 'w') as ratings_file:  # log schreiben
    ratings_file.write(json.dumps(rating))
with open('ratings.json', 'r') as data:
    js = data.readline()
    ratings = json.loads(js)
key_list = list(skill.keys())
val_list = list(skill.values())

rating = {}
for i in skill:
    rating[i] = 0
# print(lib.skill)
with open('ratings.json', 'w') as ratings_file:  # log schreiben
    ratings_file.write(json.dumps(rating))

def fight(player1, player2):
    #print(skill[player1], skill[player1], skill[player2])
    range = skill[player1]/(skill[player1] + skill[player2])

    zufall = random.uniform(0,1)
    #print(zufall)
    if zufall <= range:
        return player1
    else:
        return player2

def point_update(winner, looser):

    with open('ratings.json', 'r') as data:
        js = data.readline()
        pointsjs = json.loads(js)

    import numpy as np

    # Werte initialisieren
    alt_winner = np.array([pointsjs[winner]])
    alt_looser = np.array([pointsjs[looser]])
    exponent = 0.005

    print(pointsjs[winner], pointsjs[looser])
    # Berechnung durchführen
    pointsjs[winner] = (np.round(alt_winner + np.power(2, (alt_winner - alt_looser) * exponent), 10))[0]
    pointsjs[looser] = (np.round(alt_looser - np.power(2, (alt_looser - alt_winner) * exponent), 10))[0]


    print(pointsjs[winner], pointsjs[looser])

    with open('ratings.json', 'w') as ratings_file:
        ratings_file.write(json.dumps(pointsjs))

def rating_update():
    with open('ratings.json', 'r') as data:
        js = data.readline()
        ratings = json.loads(js)
    return ratings

def plot(dic):


    for i in dic:

        array = []
        for a in range(len(dic[i])-1):
            array.append(a)
            #print(np.array(array),np.array(log[i]))
        dic[i].pop(0)


        plt.plot(np.array(array),np.array(dic[i]), label=i)


    plt.legend()
    plt.show()


def checkKey(dic, key):
    if key in dic:
        return 1
    else:
        return 0