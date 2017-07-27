import sys
import re
from collections import Counter


def top_ip(file)
        
log_fh = open(sys.argv[1], 'r')

#s = []
#s = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",log_fh.read())

ip_counter = {}
for ip in re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",log_fh.read()):
    if ip in ip_counter:
       ip_counter[ip] += 1
    else:
       ip_counter[ip] = 1


print dict(Counter(ip_counter).most_common(10))



