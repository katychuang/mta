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


def saveFile(db, outfile):

    # Assuming db is a flat list
    with open(outfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')

        for val in db:
            writer.writerow(val)



data = openFile('rawdata/turnstile_140607.txt')

Y = []
for x in data:
    if (len(x)>0):
        Y += splitRow(x)

saveFile(Y, "x.txt")

print str(len(data)) + " rows read from this file."




