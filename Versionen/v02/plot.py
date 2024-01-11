import matplotlib.pyplot as plt
import numpy as np
import math
import json
import ast

def plot():
    with open('log.json', 'r') as data:
        js = data.readline()
        #print(type(js))
        log = ast.literal_eval(js)
    print(log)

    for i in log:
        n=1
        array = []
        for a in log[i]:
            array.append(n)
            n+=1
            #print(np.array(array),np.array(log[i]))
        plt.plot(np.array(array),np.array(log[i]), label=i)


    plt.legend()
    plt.show()
