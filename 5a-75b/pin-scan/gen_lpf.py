#!/usr/bin/env python3

import binascii
import csv
import sys

blacklist = [
	'PROGRAMN',
]

cr = csv.reader(open(sys.argv[1], 'r'))

with open(sys.argv[2], 'w') as lpf, open(sys.argv[3], 'wb') as rom:
	i = 0
	for l in cr:
		if not l[0].isdigit():
			continue
		if not l[7].isalnum():
			continue
		if l[1][0:2] not in ('PT', 'PB', 'PL', 'PR'):
			continue
		if l[1] in blacklist:
			continue

		name = l[1]
		pad  = l[7]

		lpf.write('LOCATE COMP "pads[%d]" SITE "%s";\t# %s\n' % (i, pad, name))
		lpf.write('IOBUF PORT "pads[%d]" PULLMODE=UP;\n' % (i,))
		rom.write((binascii.b2a_hex(pad.encode('utf-8')) + b'00')[0:6] + b'\n')

		i=i+1
