import re 
def _remove_regex(input_text, regex_pattern):
    res = re.findall(regex_pattern, input_text)
    return res
#    urls = re.finditer(regex_pattern, input_text) 
#    for i in urls: 
#        input_text = re.sub(i.group().strip(), '', input_text)
#    return input_text

regex_pattern = "#[\w]*"  
result = _remove_regex("remove this #hashtag from analytics vidhya", regex_pattern)
for i in result:
    print i

print result[0]

from fuzzywuzzy import process

def get_matches(query, choices, limit=4):
    result = process.extract(query, choices, limit=limit)
    return result
#text =  "remove this #hashtag123.45 15.65 from analytics vidhya"
#data = text.split()
#print data
#print type(data)
text = open('filteredtext.txt')
line = text.read()
data = line.split()

# Rs., ₹, B.No., MFD., EXP.
check = ["Rs.", "B.No.", "MFD.", "EXP.", "M.R.P. Rs.", "M.R.P.", "MFG.", "Maximum Retail Price", "Mfg. Date", "Exp. Date",] 
for names in check:
    res = get_matches(names,  data)
    print res
    num = ""
    value = 0
    val = ""
    for i in res:
        tup = i
        if tup[1] >= value:
            value = tup[1]
            val = tup[0]

#val = str(res[0][0])
    count = -1
    indexes = 0
#    for i in val:
    for i in res[0][0]:
        count = count + 1 
        if i.isdigit():
            indexes = count
            break
        

    print num
#print val        
    print val[indexes:] 
    print res[3][0].replace(names, '', 1)
#    print res[0][0][indexes:]                     
#new_segment code here  
    list_of_words = data
    next_word = list_of_words[list_of_words.index(val) + 1]
#    next_word = list_of_words[list_of_words.index(res[0][0]) + 1]
    print next_word





