import sys
import re
import collections

def generateDicts(log_fh):
    currentDict = {}
    for line in log_fh:
        if line.startswith(matchIP(line)):
            if currentDict:
                yield currentDict
            #currentDict = {"ip":line.split("_")[0][:19],"type":line.split("-",5)[3],"text":line.split("-",5)[-1]}
            currentDict = {"ip":line}
        #else:
        #    currentDict["text"] += line
    yield currentDict
    
    
def matchIP(line):
        matchThis = ""
        s = []
        matched = re.match(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',line)  
        print line
        s = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",line)
        #s = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        #counter = collections.Counter(s)
        #print s                
        
        word_counter = {}
        for word in s:
         print word
         if word in word_counter:
            word_counter[word] += 1
         else:
            word_counter[word] = 1
        
        popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
        
        top_3 = popular_words[:3]
        #print top_3
        #sys.exit(1)
        #print(counter.most_common())        
        if matched:
            #matches a date and adds it to matchThis            
            matchThis = matched.group() 
        else:
            matchThis = "NONE"
        return matchThis
        
with open(sys.argv[1], 'r') as f:
    print (list(generateDicts(f)))