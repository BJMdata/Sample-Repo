#chris reeves tutorial 8a make files
#BJMdata modifications include:
#   Python 3.5.1 update
#   Iterations control (limit to 100)
#   Conversion of timestamp to actual date time

import urllib
import re
import json
# The following module is for the sys.exit statement
import sys
# To print the actual time stamp, use:
import datetime

symbolslist = open("symbols.txt").read()
symbolslist = symbolslist.split("\n")

# for symbol in symbolslist:

# Limit iterations
for i, symbol in enumerate(symbolslist, start=1):
    # Make dynamic files
    myfile = open ("daily_prices/" + symbol + ".txt", "w+")
    myfile.close()
    url = "http://www.bloomberg.com/markets/chart/data/1D/" + symbol + ":US"
    htmlfile = urllib.request.urlopen(url)
    htmltext = htmlfile.read().decode('iso-8859-1')
    # "Json.loads" takes str instance containing a JSON document
    # Json gives an associative array (key:value pairs)
    data = json.loads(htmltext)
    datapoints = data['data_values']
    # Append to the file
    myfile = open ("daily_prices/" + symbol + ".txt", "a")
    # In the last tuple (epoch, price) in the datapoints array,
    # Print the second element (price) 
    # Print just last price for the day
    # Print all the prices every minute for the day.
    for point in datapoints:
        # Convert timestamp to actual date and time
        #date_time = datetime.datetime.fromtimestamp(point[0]/1e3)
        # Write data to the file in string CSV format (has comma delimiters)
        myfile.write( str(symbol) + "," + str(point[0]) + "," + str(point[1]) + "\n" )
    myfile.close()
    # Limit iterations to 10000
    if i % 10000 == 0:
        print "{0} records".format(i)
        break



