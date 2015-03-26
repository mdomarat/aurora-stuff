import sys
import urllib2
import re

def striphtml(data):
  p=re.compile(r'<.*?>')
  return p.sub('', data)

def get_next(page):
  return striphtml(next(page)).strip()

f = sys.argv[1]
root = f.split('.')[0]
first = True
for x in open(f,'r'): 
    crn = x.strip()
    if first:
      first = False
      term = crn
    else:
      url = 'https://aurora.umanitoba.ca/banprod/bwckschd.p_disp_detail_sched?term_in=' + term + '&crn_in=' + crn 
      page = urllib2.urlopen(url)
      for line in page:
        line = striphtml(line)
        if crn in line:
          print line.strip()
        if 'Seats' in line:
          l1 = get_next(page) 
          l2 = get_next(page) 
          l3 = get_next(page) 
          print 'capacity',l1,'actual',l2,'remaining',l3 
          break
