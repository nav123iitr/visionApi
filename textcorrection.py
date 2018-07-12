from textblob import TextBlob
text=open("textnlp.txt")
line=text.read()
words=line.split()
res = ""
for name in words:
    res = res + name + " "
print res
#blob = TextBlob('Analytics Vidhya is a gret platfrm to learn data scence')
blob = TextBlob(res)
print (blob.correct())
text1 = open("corrected.txt","w")
text1.write(blob.correct())
