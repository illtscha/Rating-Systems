x = {"Uschi": [2,3,4], "Amelie": [239,3,19], "Luis": [204,4,7], "Jakob": [3,5,6]}
print()
print({k: v for k, v in sorted(x.items(), key=lambda item: item[1][-1])})