#!/usr/bin/python

import sys
import re

def main():
    pattern = re.compile('.*ParOldGen: \d+K->(\d+)K.*PSPermGen: \d+K->(\d+)K')
    oldgen = 0
    permgen = 0
    counter = 0 
    with open(sys.argv[1]) as f:
        for line in f:
            r = pattern.search(line)
            if r is not None:
                oldgen += int(r.group(1))
                permgen += int(r.group(2))
                counter += 1 
    if counter == 0:
        print 'No matching gc records found.'
        print 'Did you choose the correct GC (-XX:UseParallelGC or -XX:UseParallelOldGC)?'
        print 'Did you enable GC Details (-XX:+PrintGCDetails)?'
    else:
        avg_oldgen = int(round((oldgen/counter),0))
        avg_permgen = int(round((permgen/counter),0))
        print 'Mean OldGen size: {0}K ({1}M)'.format(avg_oldgen, avg_oldgen/1024)
        print 'Mean PermGen size: {0}K ({1}M)'.format(avg_permgen, avg_permgen/1024)
        print
        print 'Values calculated from {0} Full GCs'.format(counter)
	
if __name__ == "__main__":
    # first check if mandatory parameters are given
    if len(sys.argv) < 2:
        exit('Usage: ' + sys.argv[0] + ' gclogfile')
    main()
