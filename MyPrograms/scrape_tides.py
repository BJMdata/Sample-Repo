# BJMdata
# scrape tides 2
# Scrape Low Tide for entered date.

import urllib
import re

# Enter date
date = raw_input('Enter date: ')

site = 'http://tides.mobilegeographics.com/locations/3220.html'
tags = ["<title>(.+?)</title>","<h2>(.+?)</h2>","2016-03-29(.+?)Low Tide"]

i = 0
print date
while i < len(tags):
    htmlfile = urllib.urlopen(site)
    htmltext = htmlfile.read()
    # get everything between the tags
    regex = tags[i]
    # convert the regex string into something that can be interpreted
    pattern = re.compile(regex)

    tides = re.findall(pattern,htmltext)
    print tides
    i += 1


