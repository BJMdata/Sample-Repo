# BJMdata
# scrape tides 1
# Scrape just the title

import urllib
import re

urls = ['http://tides.mobilegeographics.com/locations/3220.html']
i = 0

# get everything between the tags
# regex = '<title>(.+?)</title>'
regex = '<h1>(.+?)</h1>'

# convert the regex string into something that can be interpreted
pattern = re.compile(regex)

while i < len(urls):
    htmlfile = urllib.urlopen (urls[i])
    htmltext = htmlfile.read()
    tides = re.findall(pattern,htmltext)
    print tides
    i += 1


