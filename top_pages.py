import sys
import re
from collections import Counter

log_fh = open(sys.argv[1], 'r')

s = []
regex = '"(.*?)" '
s = re.findall(regex, log_fh.read())

req_counter = {}
for req in s:
    print req
#    if req in req_counter:
#       req_counter[req] += 1
#    else:
#      req_counter[req] = 1


#print dict(Counter(req_counter).most_common(10))


#line = '172.16.0.3 - - [25/Sep/2002:14:04:19 +0200] "GET / HTTP/1.1" 401 - "" "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020827"'
#regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'
#regex = '"(.*?)" (\d+)'
#regex = '"(.*?)" '


#s=re.findall(regex, log_fh.read())
#print s