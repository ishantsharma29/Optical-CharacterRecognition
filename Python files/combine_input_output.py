#!/usr/bin/env python

import sys
import csv
from itertools import izip
def construct_line( label, line ):
	new_line = []
	#if float( label ) == 0.0:
	#label = "0"
	new_line.append( label )
	for i, item in enumerate( line ):
		if item == '' or float( item ) == 0.0:
			continue
		new_item = "%s:%s" % ( i+1, item )
		new_line.append( new_item )
	new_line = " ".join( new_line )
	new_line += "\n"
	return new_line
# ---
input_file = sys.argv[1]
output_file = sys.argv[2]
sample_output_file=sys.argv[3]

try:
	label_index = int( sys.argv[4] )
except IndexError:
	label_index = 0
try:
	skip_headers = sys.argv[5]
except IndexError:
	skip_headers = 0	

i = open( input_file )
j = open( sample_output_file )
o = open( output_file, 'wb' )

reader = csv.reader( i )
reader1 = csv.reader( j )
if skip_headers:
	headers = reader.next()
for line, line1 in izip(reader, reader1):
	#if label_index == -1:
	#	label = 1
	#else:
	label = line1.pop( label_index )
	#print label
	new_line = construct_line( label, line )
	o.write( new_line )
