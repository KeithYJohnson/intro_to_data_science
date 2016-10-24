import sys
import string
import logging

HEADER_STRING = ",UNIT,DATEn,TIMEn,Hour,DESCn,ENTRIESn_hourly,EXITSn_hourly,maxpressurei,maxdewpti,mindewpti,minpressurei,meandewpti,meanpressurei,fog,rain,meanwindspdi,mintempi,meantempi,maxtempi,precipi,thunder"
HEADERS = HEADER_STRING.split(",")
UNIT_INDEX = HEADERS.index('UNIT')
ENTRIESN_HOURLY_INDEX = HEADERS.index('ENTRIESn_hourly')


def mapper():


    for line in sys.stdin:
        if "UNIT,DATEn,TIMEn,Hour,DESCn,ENTRIESn_hourly" in line:
            continue

        data = line.split(",")
        unit = data[UNIT_INDEX]
        entriesn_hourly = data[ENTRIESN_HOURLY_INDEX]

        if unit and entriesn_hourly:
            print "{0}\t{1}".format(unit,entriesn_hourly)



mapper()
