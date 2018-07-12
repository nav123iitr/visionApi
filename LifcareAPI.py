import json
import requests
text = open("onename.txt")
line = text.read()
words = line.split()
res = ""
for r in words:
    res = res + str(r+" ")
parameters = {'q':res, 'size':3}
#text = open("filteredtext.txt")
#line = text.read()
#words = str(line.split())  
#print type(line)          
response = requests.get("http://sandbox.lifcare.in/v6/catalog/medicine/search", params = parameters)
data = response.content   # .json() or .content the json 
data1 = json.loads(data) # dumps converts python object into string(which is a JSON format) and loads convert strings to python objects
file_name = open("medname.txt", "w") 
file_name.write(response.content)
#print data
file_name.close()
val = [] #############changes here also
count = -1
#print data1
#print res
#print parameters
#print type(data1)
#don't use .keyname format use ["keyname"] don't know why??????????
#print data1["payload"]["content"][0]["name"] 
for k in data1["payload"]["content"]:
    val.append(k["name"]) ###########changes here also
###########    print k["name"]   #to print name of medicines
p1 = "" 
p1 = raw_input("Select the input:" + '\t'.join(val) + "\n").strip()
for n in data1["payload"]["content"]:
    count = count + 1
    if n["name"]==p1:
        break
#len(), type(), .keys() are great to know about the Json responses
#for i in data1["payload"]["content"][0]["salts"]:
#    print i["name"]
###########changes start
#for i in data1["payload"]["content"]:
#    res = i["salts"]
#    for n in res:
#        print n["name"] #to print salts name
###########changes end
i = data1["payload"]["content"][count]    
res = i["salts"]
print "SALT_CONTENTS:"
for n in res:
    print "Name:-", n["name"], "\t", "Classification:-", n["classification"]  

