import lib
import json
import pandas as pd

export = {}

columns = ['skill']

rating = {}



if __name__ == '__main__':
    #open('log.txt', 'w').close()
    #open('ratings.json', 'w').close()

    for i in lib.skill:
        rating[i] = 0
    #print(lib.skill)
    #with open('ratings.json', 'w') as ratings_file:  # log schreiben
        #ratings_file.write(json.dumps(rating))

    with open('stärke.json', 'r') as data:
        js = data.readline()
        skill = json.loads(js)
    #with open('ratings.json', 'r') as data:
        #js = data.readline()
        #ratings = json.loads(js)

    key_list = list(skill.keys())
    val_list = list(skill.values())


    for i in range(100):
        lib.key_list = list(lib.skill.keys())

        n_gesamt = len(lib.skill)  # anzahl der personen mit skill #10
        ohneletzten = lib.key_list[:-1]  # liste ohne letzte person

        for player in ohneletzten:
            temp = list(lib.ratings.items())
            res = [idx for idx, key in enumerate(temp) if key[0] == player]

            #print(n_gesamt, res[0], 1)

            for opponent in range(n_gesamt - res[0] - 1):

                winner = lib.fight(player, lib.key_list[opponent + 1])

                if winner == player:#wenn i gewonnen hat
                    looser = lib.key_list[opponent+1]#dann ist der verlierer der andere
                elif winner == lib.key_list[opponent+1]:#wenn der andere gewonnen hat
                    looser = player#dann ist der verlierer i

                rating = lib.point_update(winner, looser, rating)
                #with open('log.txt', 'a') as f:#log schreiben
                #    f.write("\nWinner: %s %s +1 Looser: %s %s -1"%(winner,rating[winner],looser,rating[looser]))#log schreiben

                if lib.checkKey(export, winner):
                    export[winner].append(rating[winner])
                else:
                    export[winner] = [lib.skill[winner], 0, rating[winner]]
                if lib.checkKey(export, looser):
                    export[looser].append(rating[looser])
                else:
                    export[looser] = [lib.skill[looser], 0, rating[looser]]
            #pass
            lib.key_list.pop(0)
        print(f"Round {i+1} finished")

    lib.key_list = list(skill.keys())

    for num in range(len(export[lib.key_list[0]]) - 1):
        columns.append(num)


    df = pd.DataFrame(export)
    df.index = columns
    df = df.T

    skills = []
    for skill in lib.skill:
        skills.append(lib.skill[skill])

    file_name = '_'.join(map(str, skills)) + '_file.csv'

    df.to_csv()
    df.to_csv("1hourfile.csv")  # file_name)

    lib.plot(export)