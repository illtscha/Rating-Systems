import random
import pandas as pd
import json
import lib


export = {}

columns = ['skill']

rating = {}

if __name__ == '__main__':
    open('log.txt', 'w').close()
    open('ratings.json', 'w').close()
    for i in lib.skill:
        rating[i] = 0
    #print(lib.skill)
    with open('ratings.json', 'w') as ratings_file:  # log schreiben
        ratings_file.write(json.dumps(rating))

    with open('stärke.json', 'r') as data:
        js = data.readline()
        skill = json.loads(js)
    with open('ratings.json', 'r') as data:
        js = data.readline()
        ratings = json.loads(js)

    key_list = list(skill.keys())
    val_list = list(skill.values())
    #while(True):

    for l in range(100): #100 mal ausführen
        lib.key_list = list(skill.keys())

        n_gesamt = len(lib.skill)#anzahl der personen mit skill #10
        ohneletzten = key_list[:-1]#liste ohne letzte person
        for i in ohneletzten: #für person in liste von personen mit skill #10mal

            temp = list(lib.ratings.items())
            res = [idx for idx, key in enumerate(temp) if key[0] == i] #index von i in ratings finden
            #print(res[0])

            for a in range(n_gesamt - res[0] - 1):#für jede person die noch nicht gegen i gekämpft hat
                #print(n_gesamt - res[0] - 1, n_gesamt, res[0], 1)
                #print(i,lib.key_list[a+1])#kampf ausgeben
                #print(a)


                winner = lib.fight(i, lib.key_list[a+1])#kampf ausführen


                if winner == i:#wenn i gewonnen hat
                    looser = lib.key_list[a+1]#dann ist der verlierer der andere
                elif winner == lib.key_list[a+1]:#wenn der andere gewonnen hat
                    looser = i#dann ist der verlierer i

                #print(winner, looser)
                lib.point_update(winner, looser)#punkte updaten
                lib.rating_update()
                with open('log.txt', 'a') as f:#log schreiben
                    f.write("\nWinner: %s %s +1 Looser: %s %s -1"%(winner,lib.ratings[winner],looser,lib.ratings[looser]))#log schreiben
                ratings = lib.rating_update()  # ratings updaten
                if lib.checkKey(export, winner):
                    export[winner].append(ratings[winner])
                else:
                    export[winner] = []
                    export[winner].append(lib.skill[winner])
                    export[winner].append(0)
                    export[winner].append(ratings[winner])
                if lib.checkKey(export, looser):
                    export[looser].append(ratings[looser])
                else:
                    export[looser] = []
                    export[looser].append(lib.skill[looser])
                    export[looser].append(0)
                    export[looser].append(ratings[looser])

            lib.key_list.pop(0)



    lib.key_list = list(skill.keys())
        #print(l)
    for num in range(len(export[lib.key_list[0]])-1):
        columns.append(num)
    #print(columns)
    #print(export)
    df = pd.DataFrame(export)
    df.index = columns
    df = df.T
    skills = []
    for skill in lib.skill:
        skills.append(lib.skill[skill])
    #filename '1_3_3_file.csv'
    file_name = '_'.join(map(str, skills)) + '_file.csv'


    df.to_csv()
    df.to_csv(file_name)
    #print(file_name)
    #print("test2")
    #print(df.T)
    #print(export)
    lib.plot(export)


