#!/usr/bin/python
import argparse
__author__ = "Tom Gijselinck"


parser = argparse.ArgumentParser(description='Calculate the pace in min/km.')
parser.add_argument('-t', '--time', help='Time in mm:ss', required=True)
parser.add_argument('-d', '--distance', help='Distance in metres', required=True, type=int)
args = parser.parse_args()

m = args.time.split(':')[0]
s = args.time.split(':')[1]
total_time = int(m)*60.0 + int(s)
pace = total_time/args.distance*1000
minutes = int(pace/60)
seconds = pace%60

print ("Pace: " + str(minutes) + ":" + str(seconds))
