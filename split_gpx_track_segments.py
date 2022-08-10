#!/usr/bin/python3

# Split a multitrack gpx file into individual gpx files with a single track segment each.

import re
import gpxpy
import gpxpy.gpx
import sys

gpx_file = open(sys.argv[1], 'r')

in_gpx = gpxpy.parse(gpx_file)

for track in in_gpx.tracks:
    print(track.name)

    track.extensions = ''

    out_gpx = gpxpy.gpx.GPX()
    out_gpx.tracks.append(track)
    
    filename = re.sub('[\/\s]','-', track.name) + ".gpx"

    out_gpx_file = open(filename, 'w')
    out_gpx_file.write(out_gpx.to_xml())
    out_gpx_file.close()
