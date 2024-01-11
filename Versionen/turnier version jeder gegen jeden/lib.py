import random
import simplejson as json
import matplotlib.pyplot as plt
import numpy as np
import ast
import math

iterations = 100
kalpha=-1
alpha = 10
beta = 1
#alpha_-1_beta_0
filename = ("plots/alpha_%s_beta_%s_iter_%s" % (alpha*100, beta*100,iterations)).replace(".", "_")
filenamepoints = ("plots/alpha_%s_beta_%s_iter_%s_points" % (alpha*100, beta*100,iterations)).replace(".", "_")

with open('skill.json', 'r') as data:
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

def point_update(winner, looser, rating: dict):

    winnertemp = rating[winner]
    loosertemp = rating[looser]

    rating[winner] = winnertemp + (beta * (1 - np.tanh(alpha * (winnertemp - loosertemp))))
    rating[looser] = loosertemp - (beta * (1 + np.tanh(alpha * (loosertemp - winnertemp))))


    return rating



def rating_update():
    with open('ratings.json', 'r') as data:
        js = data.readline()
        ratings = json.loads(js)
    return ratings

def plot(dic):
    plt.title("Alpha = %s\nBeta = %s\nIter = %s" % (alpha, beta, iterations))
    for i in dic:

        array = []
        for a in range(len(dic[i])-1):
            array.append(a)
            #print(np.array(array),np.array(log[i]))
        dic[i].pop(0)


        plt.plot(np.array(array),np.array(dic[i]), label=i)

    plt.savefig(filename)
    plt.show()

def plotpoints(x,y):

    plt.title("Alpha = %s\nBeta = %s\nIter = %s" % (alpha, beta, iterations))
    plt.plot(np.array(x), np.array(y), 'o')
    plt.savefig(filenamepoints)
    plt.show()


def checkKey(dic, key):
    if key in dic:
        return 1
    else:
        return 0

def sigma_sum(start, end):
    return sum(i for i in range(start, end))