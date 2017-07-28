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
      out = ''
      for line in page:
        line = striphtml(line)
        if crn in line:
          print line.strip()
        if 'Waitlist Seats' in line:
          l1 = get_next(page) 
          l2 = get_next(page) 
          l3 = get_next(page) 
          print out,'Waitlist',l2
          break
        if 'Seats' in line:
          l1 = get_next(page) 
          l2 = get_next(page) 
          l3 = get_next(page) 
          out = 'capacity %s actual %s remaining %s' % (l1,l2,l3)
