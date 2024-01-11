
import json
import pandas as pd
import alive_progress
import threading
import random
import simplejson as json
import matplotlib.pyplot as plt
import numpy as np
import ast
import os

iterations = 10000
alpha = 0.01
beta = 0.001
gamma = 0.01
tol = 10
vector = 10

thread_no1_alpha = 0.01
thread_no2_alpha = 0.02
thread_no3_alpha = 0.03
thread_no4_alpha = 0.04
thread_no5_alpha = 0.05
thread_no6_alpha = 0.06
thread_no7_alpha = 0.07
thread_no8_alpha = 0.08
thread_no9_alpha = 0.09
thread_no10_alpha = 0.1






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

    #print(vector_rating, vector_skill)
    vector_gesamt = np.array(vector_rating) - np.array(vector_skill)
    #print(vector_gesamt)
    return np.linalg.norm(vector_gesamt)




def multi_threading(threadnum,alpha_start):
    iterations = 10000

    beta = 0.001
    gamma = 0.01
    tol = 10
    vector = 10
    alpha = alpha_start
    while True:
        if (vector > 3):
            export = {}

            columns = ['skill']




            for i in skill: #rating initialisieren
                rating[i] = 0




            persons = list(skill.keys()) #skill in liste
            val_list = list(skill.values()) #skill in liste
            h = 0

            #with alive_progress.alive_bar(iterations, force_tty=True, spinner="waves2", bar="filling") as bar:

            #while True:
            for i in range(iterations):

                player1 = random.choice(persons)
                player2 = random.choice(persons)


                iter = 0
                while (player1 == player2) or (abs(rating[player1]-rating[player2]) > (tol)):

                    player2 = random.choice(persons)
                    iter += 1
                    if iter > len(skill):
                        #player1 = random.choice(persons)
                        #print("break")
                        h =1
                        break


                if h == 1:
                    h = 0
                    #bar()
                    continue
                winner = fight(player1, player2)
                #bar()
                if winner == player1:
                    looser = player2
                elif winner == player2:
                    looser = player1

                for player in persons:
                    if player != winner and player != looser:
                        #if player does not exist in export, add him
                        if checkKey(export, player):
                            export[player].append(rating[player])
                        else:
                            export[player] = [skill[player], 0, rating[player]]

                point_update(winner, looser)


                if checkKey(export, winner):
                    export[winner].append(rating[winner])
                else:
                    export[winner] = [skill[winner], 0, rating[winner]]
                if checkKey(export, looser):
                    export[looser].append(rating[looser])
                else:
                    export[looser] = [skill[looser], 0, rating[looser]]



            #every array in export has to be the same length
            longest = max(len(l) for l in export.values())
            for i in export:
                while len(export[i]) < longest:
                    export[i].append(export[i][-1])
            #print(export)
            for num in range(len(export[persons[0]]) - 1):
                columns.append(num)
            df = pd.DataFrame(export)
            df.index = columns
            df = df.T

            skills = []
            for skil in skill:
                #print(skil)
                skills.append(skill[skil])

            file_name = '_'.join(map(str, skills)) + '_file.csv'

            #df.to_csv("1hourfile.csv")  # file_name)
            skillpoints = []
            endpoints = []
            sum = 0
            #print(export)
            export_list = list(export.keys())
            #print(export_list)
            for i in export_list:
                skillpoints.append(skill[i])
                endpoints.append(export[i][-1])
                sum += export[i][-1]
            #print(sum)
            vector = vectors()
            #print("\n\nAlpha %s\nBeta %s\nGamma %s\nIter %s\nTol %s\nVector %s" % (alpha, beta, gamma, iterations, tol, vector))
            #print("\n",threading.active_count())
            #print(beta)
            if (beta < 1):

                if (tol < 100):
                    tol += 10
                    print(tol)
                    #print("\n\nAlpha %s\nBeta %s\nGamma %s\nIter %s\nTol %s\nVector %s" % (
                    #alpha, beta, gamma, iterations, tol, vector))
                elif (tol >= 100):
                    beta = round(beta + 0.001, 3)
                    print(alpha)
                    print(beta)
                    tol = 10
            elif (beta >= 1):

                beta = 0.001
                alpha += 0.1
                print(alpha)
            #plotpoints(skillpoints, endpoints)
            #plot(export,skill)

        else:
            with open('vector.txt', 'a') as f:
                f.write("\n\n%s. Thread\nAlpha %s\nBeta %s\nGamma %s\nIter %s\nTol %s\nVector %s" % (threadnum, alpha, beta, gamma, iterations, tol, vector))
            print("found one!")
            f.close
            vector = 10



if __name__ == '__main__':
    t1 = threading.Thread(target=multi_threading, args=(1, thread_no1_alpha,))
    t2 = threading.Thread(target=multi_threading, args=(2, thread_no2_alpha,))
    t3 = threading.Thread(target=multi_threading, args=(3, thread_no3_alpha,))
    t4 = threading.Thread(target=multi_threading, args=(4, thread_no4_alpha,))
    t5 = threading.Thread(target=multi_threading, args=(5, thread_no5_alpha,))
    t6 = threading.Thread(target=multi_threading, args=(6, thread_no6_alpha,))
    t7 = threading.Thread(target=multi_threading, args=(7, thread_no7_alpha,))
    t8 = threading.Thread(target=multi_threading, args=(8, thread_no8_alpha,))
    t9 = threading.Thread(target=multi_threading, args=(9, thread_no9_alpha,))
    t10 = threading.Thread(target=multi_threading, args=(10, thread_no10_alpha,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()




