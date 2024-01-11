import ast

with open('log.json', 'r') as data:
    js = data.readline()
    print(type(js))
    log = ast.literal_eval(js)

print(len(log["Simon"]))
print(log["Simon"][-1],log["Ilija"][-1], log["Jakob"][-1],  log["Amelie"][-1], log["Luis"][-1], log["Michael"][-1])
