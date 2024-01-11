import random
import json
import matplotlib.pyplot as plt
import numpy as np
import ast


with open('stärke.json', 'r') as data:
    js = data.readline()
    skill = json.loads(js)
with open('ratings.json', 'r') as data:
    js = data.readline()
    ratings = json.loads(js)
key_list = list(skill.keys())
val_list = list(skill.values())


def fight(player1, player2):
    print(skill[player1], skill[player1], skill[player2])
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


    pointsjs[winner] = pointsjs[winner] + 1
    pointsjs[looser] = pointsjs[looser] - 1
    #print("test")
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