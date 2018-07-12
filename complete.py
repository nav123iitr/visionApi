import json
from fuzzywuzzy import process
def get_matches(query, choices, limit=1):
    result = process.extract(query, choices, limit=limit)
    return result
import pandas as pd

data_xls = pd.read_excel('4678_O. P. PHARMA_CORNER STORE TECHNOL.xls')
data_xls.to_csv('csvfile1.csv', encoding = 'utf-8', index = True)

df = pd.read_csv("csvfile1.csv")
df_list = df['ITEM NAME'].tolist()
count =-1
df_pack = df['PACK'].tolist()
df_batch = df['BATCH'].tolist()
df_expiry = df['EXPIRY'].tolist()
df_mrp = df['MRP'].tolist()
df_company = df['COMPANY'].tolist()
max = 60
# note here we will get first element whose score is greater than 60 then later values whose score is greater than the previous score will be selected
val = []
res = []
text = open('clean.txt')
line = text.read()            
words = line.split()        
for name in words:
    res = res + get_matches(name, df_list)  

#print res
text.close()
#    print res[0][0]    
#    if res[0][1]>90: 
#    print res
for i in  res:
    tup = i
    if tup[1]>=max:
        max = tup[1]
        val.append(tup[0]) 
#print val 
#print type(val)
p1 = "" 
p1 = raw_input("Select the input:" + ' '.join(val) + "\n").strip()
#print p1      
#print type(p1)
for n in df_list:
#    print n," ",p1
#    print type(n),
#    print type(p1)
#    print(len(n)),
#    print(len(p1))
    count = count + 1
    if(n.strip()==p1.strip()):
#        print "#"*80
        break
#print count    
print "Item_Name:",p1
print "Pack_Size:",df_pack[count]   
print "Batch_No.:",df_batch[count] 
print "Expiry Date:",df_expiry[count]  
print "M.R.P.",df_mrp[count]
print "Company Name:",df_company[count]      
dic = {"Item_Name":p1,"Pack_Size":df_pack[count],"Batch_No.:":df_batch[count],"Expiry Date:":df_expiry[count],"M.R.P.":df_mrp[count],"Company Name:":df_company[count] }
data1 = json.dumps(dic)
#print dic
#print type(data1)
#print data1
nameonly = open('onename.txt', 'w')
nameonly.write(p1)
nameonly.close()
