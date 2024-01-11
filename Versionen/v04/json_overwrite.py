import json

open('log.json', 'w').close()
log = {"Simon": [0], "Ilija": [0]}#, "Jakob": [0], "Amelie": [0], "Luis": [0], "Michael": [0]}
with open('log.json', 'w') as log_file:  # log schreiben
    log_file.write(json.dumps(log))  # log schreiben
    log_file.close()


open('log.txt', 'w').close()




open('ratings.json', 'w').close()
log = {"Simon": 0, "Ilija": 0}#, "Jakob": 0, "Amelie": 0, "Luis": 0, "Michael": 0}
with open('ratings.json', 'w') as ratings_file:  # log schreiben
    ratings_file.write(json.dumps(log))  # log schreiben
