import lib
import json
import pandas as pd
import alive_progress
import threading
import random

export = {}

columns = ['skill']




if __name__ == '__main__':

    for i in lib.skill: #lib.rating initialisieren
        lib.rating[i] = 0




    persons = list(lib.skill.keys()) #skill in liste
    val_list = list(lib.skill.values()) #skill in liste
    h = 0

    with alive_progress.alive_bar(lib.iterations, force_tty=True, spinner="waves2", bar="filling") as bar:

        #while True:
        for i in range(lib.iterations):

            player1 = random.choice(persons)
            player2 = random.choice(persons)


            iter = 0
            while (player1 == player2) or (abs(lib.rating[player1]-lib.rating[player2]) > (lib.tol)):

                player2 = random.choice(persons)
                iter += 1
                if iter > len(lib.skill):
                    #player1 = random.choice(persons)
                    #print("break")
                    h =1
                    break


            if h == 1:
                h = 0
                bar()
                continue
            winner = lib.fight(player1, player2)
            bar()
            if winner == player1:
                looser = player2
            elif winner == player2:
                looser = player1

            for player in persons:
                if player != winner and player != looser:
                    #if player does not exist in export, add him
                    if lib.checkKey(export, player):
                        export[player].append(lib.rating[player])
                    else:
                        export[player] = [lib.skill[player], 0, lib.rating[player]]

            lib.point_update(winner, looser)


            if lib.checkKey(export, winner):
                export[winner].append(lib.rating[winner])
            else:
                export[winner] = [lib.skill[winner], 0, lib.rating[winner]]
            if lib.checkKey(export, looser):
                export[looser].append(lib.rating[looser])
            else:
                export[looser] = [lib.skill[looser], 0, lib.rating[looser]]



    #every array in export has to be the same length
    longest = max(len(l) for l in export.values())
    for i in export:
        while len(export[i]) < longest:
            export[i].append(export[i][-1])
    #print(export)
    for num in range(len(export[lib.persons[0]]) - 1):
        columns.append(num)
    df = pd.DataFrame(export)
    df.index = columns
    df = df.T

    skills = []
    for skill in lib.skill:
        skills.append(lib.skill[skill])

    file_name = '_'.join(map(str, skills)) + '_file.csv'

    #df.to_csv("1hourfile.csv")  # file_name)
    skillpoints = []
    endpoints = []
    sum = 0
    #print(export)
    export_list = list(export.keys())
    #print(export_list)
    for i in export_list:
        skillpoints.append(lib.skill[i])
        endpoints.append(export[i][-1])
        sum += export[i][-1]
    #print(sum)
    print(lib.vectors())
    #lib.plotpoints(skillpoints, endpoints)
    lib.plot(export,lib.skill)