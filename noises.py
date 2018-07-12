import io

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english')) #list word is added
#list1 = ['each', 'veg', 'capsule', 'other', 'ingredients', 'recommended', 'usage', 'directed', 'healthcare', 'professional', 'store', 'below', 'keep', 'reach', 'children','product', 'intended', 'diagnose', 'treat', 'cure', 'prevent', 'disease', 'medicinal', 'use', 'manufacture', 'marketed'] #add a line
#stop_words = stop_words.append(list1) #add a line
file1 = open("text.txt")
line = file1.read()# Use this to read file content as a stream:
words = line.split()
appendFile = open('filteredtext.txt','w+')
for r in words:
    if not r in stop_words:
#        appendFile = open('filteredtext.txt','w')
#        appendFile.write(" "+r)
        appendFile.write('\n' + r)
#        appendFile.close()
appendFile.close()

content = open('filteredtext.txt', 'r').readlines()
content_set = set(content)
cleandata = open('clean.txt', 'w')
for line in content_set:
    cleandata.write(line)
cleandata.close()

  
