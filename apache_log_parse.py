import sys
import re
from collections import Counter
from collections import OrderedDict
from apachelog import *
import operator
from operator import itemgetter
import argparse

def top_10_requests(file):
    log_fh = open(file, 'r')
    requests_d = {}
    log = apache_log(log_fh)
    request = list(r['request'] for r in log)

    for req in request: 
        if not req in requests_d:
            requests_d[req] = 1
        else:
            requests_d[req] += 1

    sorted_requests = OrderedDict(sorted(requests_d.items(), key=itemgetter(1),reverse=True))  

    count = 0
    print "Top 10 requests:\n" 
    for key in sorted_requests:
        if count <= 10:    
         print(key, sorted_requests[key])
         count += 1
    sys.exit(0)
 

def top_10_ips(file):
    log_fh = open(file, 'r')
    ips_d = {}
    log = apache_log(log_fh)
    hosts = list(r['host'] for r in log)
    for ip in hosts:         
        if not ip in ips_d:
            ips_d[ip] = 1            
        else:
            ips_d[ip] += 1                        

    sorted_ips = OrderedDict(sorted(ips_d.items(), key=itemgetter(1),reverse=True))  

    count = 0
    print "Top 10 ips:\n" 
    for key in sorted_ips:
        if count <= 10:    
         print(key, sorted_ips[key])
         count += 1
    sys.exit(0)
    
def top_10_fail_requests(file):
    log_fh = open(file, 'r')
    requests_d = {}
    log = apache_log(log_fh)
    request = list(r['request'] for r in log
                if (599 <= r['status'] >= 400 or 199 <= r['status'] >= 100))

    for req in request: 
        if not req in requests_d:
            requests_d[req] = 1
        else:
            requests_d[req] += 1

    sorted_requests = OrderedDict(sorted(requests_d.items(), key=itemgetter(1),reverse=True))  

    count = 0
    print "Top 10 fail requests:\n" 
    for key in sorted_requests:
        if count <= 10:    
         print(key, sorted_requests[key])
         count += 1
    sys.exit(0)
    
def percent_fail_requests(file):
    log_fh = open(file, 'r')
    
    num_req = open(file, 'r')
    num_lines = sum(1 for line in num_req)  
    
    
    requests_d = {}
    log = apache_log(log_fh)
    request = list(r['request'] for r in log
                if (599 <= r['status'] >= 400 or 199 <= r['status'] >= 100))

    for req in request: 
        if not req in requests_d:
            requests_d[req] = 1
        else:
            requests_d[req] += 1

    
    print 'bad request number: ' + str(len(requests_d))
    print 'which is '+ str(int(float(float(len(requests_d)) / float(num_lines) * 100)))+'%'
    sys.exit(0)
    
def percent_successful_requests(file):
    log_fh = open(file, 'r')
    
    num_req = open(file, 'r')
    num_lines = sum(1 for line in num_req)  
    
    
    requests_d = {}
    log = apache_log(log_fh)
    request = list(r['request'] for r in log
                if (299 <= r['status'] >= 200 or 399 <= r['status'] >= 300))

    for req in request: 
        if not req in requests_d:
            requests_d[req] = 1
        else:
            requests_d[req] += 1

    
    print 'successful request number: ' + str(len(requests_d))
    print 'which is '+ str(int(float(float(len(requests_d)) / float(num_lines) * 100)))+'%'
    sys.exit(0)
 
 
def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--l', metavar='string', help='log file path',)
    parser.add_argument('--tr10', help='top 10 requests',type=str)
    parser.add_argument('--tip10',
                        help='top 10 ips')
    parser.add_argument('--tf10', 
                        help='top 10 fail requests')
    parser.add_argument('--pf',
                        help='Percent of fail requests')
    parser.add_argument('--ps',
                        help='Percent of successfull requests')
    args = parser.parse_args()
    return vars(args)

    
 
def main():
 args = command_line_args()
 file = args['l']
 t10 = args['tr10']
 tip10 = args['tip10']
 tf10 = args['tf10']
 pf = args['pf']
 ps = args['ps'] 
 if t10:
    top_10_requests(file)
 if tip10:
    top_10_ips(file)
 if tf10:
    top_10_fail_requests(file)
 if pf:
    percent_fail_requests(file)
 if ps:
    percent_successful_requests(file)
    
    
# main routine
if __name__=='__main__':
  main()
 
#top_10_requests(sys.argv[1])
#top_10_ips(sys.argv[1])
#top_10_fail_requests(sys.argv[1])
#percent_fail_requests(sys.argv[1])
#percent_successful_requests(sys.argv[1])