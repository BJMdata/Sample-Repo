# get_rt22_no_blanks.py
#
# Inspired by David Beazley Video - Python thru public data hacking
# http://www.dabeaz.com/pydata/
# This program reads an xml data file from transit system website
#  then writes one of the bus routes to a file rt22.xml.
#  BJMdata modified it for:
#   wrote a new file rt22c.xml with all the blank lines stripped,
#   and with a readable date/time appended.

import urllib
from datetime import datetime

site = 'http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22'
u = urllib.urlopen(site)
data = u.read()

# Write the binary ('wb') xml data file 
fi = open('rt22.xml', 'wb')
fi.write(data)
#fi.close()

print ('Wrote rt22.xml')

# Open a new file to which to write the compacted data
fi = open('rt22.xml', 'r')
fc = open('rt22c.xml', 'w')

# Write ('w') the data file with current date and time
today = str(datetime.now()) + "\n"
fc.write(today)

# Now strip any blank lines from that file...
for line in fi:
  # Use rstrip instead of strip so you don't strip any indentation
  line = line.rstrip()
  if line != '':
    fc.write(line + "\n")
fi.close()
fc.close()

print ('Wrote rt22c.xml with date/time and no blank lines')
