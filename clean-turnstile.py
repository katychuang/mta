#!/usr/bin/env python

""" This module includes helper functions for cleaning and extracting MTA turnstile data.
"""

import csv

__author__ = "Kat Chuang @katychuang"
__copyright__ = "Copyright 2014"
__credits__ = ["Kat Chuang"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Kat Chuang"
__email__ = "katychuang@gmail.com"
__status__ = "Development"


def splitRow(x):

    audits = []
    for i in range(4, 43):
        if i in [4, 9, 14, 19, 24, 29, 34, 39]:
                audits.append(x[0:3] + x[i:i+4])

    return audits

def openFile(filename):
    with open(filename, 'rb') as csvfile:
        stripped = (row.strip() for row in csvfile)
        subwayReader = csv.reader(stripped, delimiter=',', quotechar='"')
        data = [row for row in subwayReader]
    return data


data = openFile('rawdata/turnstile_140705.txt')

Y = []
for x in data[:10]:
    if (len(x)>0):
        audit = splitRow(x)
        for x in audit:
            print x

print str(len(data)) + " rows read from this file."




