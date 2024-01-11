import random
import simplejson as json
import matplotlib.pyplot as plt
import numpy as np
import ast
import math

iterations = 100000
alpha = 0.01
beta = 0.012000000000000004
gamma = 0.01
tol = 40



with open('skill.json', 'r') as data:
    js = data.readline()
    skill = json.loads(js)
skill = {k: v for k, v in sorted(skill.items(), key=lambda item: item[1], reverse=True)}

filename = ("plots/alpha_%s_beta_%s_%s_gamma_iter_%s" % (alpha*100, beta*100,gamma*100,iterations)).replace(".", "_")
filenamepoints = ("plots/alpha_%s_beta_%s_iter_%s_points" % (alpha*100, beta*100,iterations)).replace(".", "_")


rating = {}

persons = list(skill.keys())
val_list = list(skill.values())

for i in skill:
    rating[i] = 0


def fight(player1, player2):
    #print(skill[player1], skill[player1], skill[player2])
    range = skill[player1]/(skill[player1] + skill[player2])

    zufall = random.uniform(0,1)
    #print(zufall)
    if zufall <= range:
        Winner = player1
        Looser = player2
    else:
        Winner = player2
        Looser = player1

    #if both are equal give both one point
    if skill[player1] == skill[player2]:
        skill[player1] += 1
        skill[player2] += 1
        return Winner
    else:
        if player1 <= player2:
            bigger = player2
            smaller = player1
        if player1 > player2:
            bigger = player1
            smaller = player2


        skill[bigger] = skill[bigger]+((skill[smaller]/skill[bigger])*gamma)
        skill[smaller] = skill[smaller]+((skill[bigger]/skill[smaller])*gamma)
        return Winner

def point_update(winner, looser):

    winnertemp = rating[winner]
    loosertemp = rating[looser]


    rating[winner] = winnertemp + ((1 - np.tanh(alpha * (winnertemp - loosertemp)))*beta)
    rating[looser] = loosertemp - ((1 + np.tanh(alpha * (loosertemp - winnertemp)))*beta)






def plot(dic, skill):
    plt.title("Alpha = %s\nBeta = %s\nGamma = %s\nIter = %s" % (alpha, beta, gamma, iterations))
    end_order = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1][-1], reverse=True)}
    list = []
    for i in end_order:

        list.append(i)
    new_sorted_skill = {k: v for k, v in sorted(skill.items(), key=lambda item: item[1], reverse=True)}
    #list of new_sorted_skill keys
    skill_list = []
    for i in new_sorted_skill:
        skill_list.append(i)
    place = 1
    for i in skill:

        array = []
        for a in range(len(dic[i])-1):
            array.append(a)
            #print(np.array(array),np.array(log[i]))
        dic[i].pop(0)


        plt.plot(np.array(array),np.array(dic[i]), label=("%s. %s, %ser %ser"%(place,i, skill_list.index(i)+1, list.index(i)+1)))
        place += 1
    plt.legend()
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

#find lenght of skill vector minus rating vector and first create both vectors
def vectors():
    end_rating_order = {k: v for k, v in sorted(rating.items(), key=lambda item: item[1], reverse=True)}

    rating_placement = []
    for i in end_rating_order:
        rating_placement.append(i)
    end_skill_order = {k: v for k, v in sorted(skill.items(), key=lambda item: item[1], reverse=True)}

    # list of new_sorted_skill keys
    skill_placement = []
    for i in end_skill_order:
        skill_placement.append(i)
    vector_rating = []
    vector_skill = []
    for i in end_rating_order:

        vector_rating.append(rating_placement.index(i) + 1)
        vector_skill.append(skill_placement.index(i) + 1)
    vector_rating = np.array(vector_rating)
    vector_skill = np.array(vector_skill)

    print(vector_rating, vector_skill)
    vector_gesamt = np.array(vector_rating) - np.array(vector_skill)
    print(vector_gesamt)
    return np.linalg.norm(vector_gesamt)


