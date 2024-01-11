import os
import json
with open('skill.json', 'r') as data:
    js = data.readline()
    skill = json.loads(js)
print(skill)
