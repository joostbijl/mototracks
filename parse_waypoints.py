#!/usr/bin/python3

# This script filters waypoints from a GPX file. Purpose is to only find 'SG 4' or 'SG 5' waypoints (according to Denzel)

import re
import sys
import gpxpy
import gpxpy.gpx

# https://alpenrouten.de/downloads.html download the file here: GPX-Datei mit vollen Namen
in_gpx_file = open(sys.argv[1], 'r')
in_gpx = gpxpy.parse(in_gpx_file)

out_gpx_file = open(sys.argv[2], 'w')
out_gpx = gpxpy.gpx.GPX()

for waypoint in in_gpx.waypoints:
    
    # Find SG 4 and 5 (this also finds SG 4-5)
    if (re.findall(r'(SG\s+5|SG\s+4)', waypoint.comment)):
        print('--> {1} ({0})'.format(waypoint.comment, waypoint.name))
        out_gpx.waypoints.append(waypoint)

out_gpx_file.write(out_gpx.to_xml())
out_gpx_file.close()
