#!/usr/bin/env python3

import binascii
import csv
import argparse

blacklist = [
    'PROGRAMN',
]

PACKAGES = {
        'CABGA381': 7,
        'CABGA285': 8,
        'CABGA256': 9
}

parser = argparse.ArgumentParser()
parser.add_argument("pinout", help="The pinout file")
parser.add_argument("lpf", help="The output LPF file")
parser.add_argument("rom", help="The output .hex file")
parser.add_argument("--package", help="The target package",
                    choices=PACKAGES.keys())

args = parser.parse_args()

cr = csv.reader(open(args.pinout, 'r'))

with open(args.lpf, 'w') as lpf, open(args.rom, 'wb') as rom:
    i = 0
    for l in cr:
        if not l[0].isdigit():
            continue
        if not l[PACKAGES[args.package]].isalnum():
            continue
        if l[1][0:2] not in ('PT', 'PB', 'PL', 'PR'):
            continue
        if l[1] in blacklist:
            continue

        name = l[1]
        pad  = l[PACKAGES[args.package]]

        lpf.write('LOCATE COMP "pads[%d]" SITE "%s";\t# %s\n' % (i, pad, name))
        lpf.write('IOBUF PORT "pads[%d]" PULLMODE=UP;\n' % (i,))
        rom.write((binascii.b2a_hex(pad.encode('utf-8')) + b'00')[0:6] + b'\n')

        i = i+1
