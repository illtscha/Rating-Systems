import pandas as pd

data = {
    'name': ['John Doe', 'Jane Doe'],
    'age': [30, 28]
}
columns = ['name1', 'age1']

df = pd.DataFrame(data)
df.index = columns

print(df)
df.to_csv('file.csv')
