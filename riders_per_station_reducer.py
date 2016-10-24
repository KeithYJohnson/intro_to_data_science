import sys
import logging

def reducer():

    entriesn_hourly_per_unit = {}
    for line in sys.stdin:
        unit, entriesn_hourly = line.split("\t")
        entriesn_hourly = float(entriesn_hourly)

        if not unit and entriesn_hourly:
            continue


        if unit in entriesn_hourly_per_unit.keys():
            entriesn_hourly_per_unit[unit] += entriesn_hourly
        else:
            entriesn_hourly_per_unit[unit] = entriesn_hourly


    for key in entriesn_hourly_per_unit:
        print "{0}\t{1}".format(key, entriesn_hourly_per_unit[unit])



reducer()
