from fuzzywuzzy import process
def get_matches(query, choices, limit=1):
    result = process.extract(query, choices, limit=limit)
    return result
import pandas as pd
df = pd.read_csv("salt123.csv")
#names = df.name
#print names
#print type(names)
df_list = df['name'].tolist()
#print df_list

text = open('textnlp.txt')
line = text.read()
words = line.split()
for name in words:
    if name!="":
        res = get_matches(name, df_list)
    if res[0][1]>90:
        print res[0][0] 
        