import sys
import string
import logging

# from util import mapper_logfile
# logging.basicConfig(filename=mapper_logfile, format='%(message)s',
#                     level=logging.INFO, filemode='w')

HEADER_LINE ="Registrar,Enrolment Agency,State,District,Sub District,Pin Code,Gender,Age,Aadhaar generated,Enrolment Rejected,Residents providing email,Residents providing mobile number"
HEADER_LIST = HEADER_LINE.split(',')
DISTRICT_INDEX = HEADER_LIST.index("District")
AADHAAR_GENERATED_INDEX = HEADER_LIST.index("Aadhaar generated")
def mapper():
    #Also make sure to fill out the reducer code before clicking "Test Run" or "Submit".

    #Each line will be a comma-separated list of values. The
    #header row WILL be included. Tokenize each row using the
    #commas, and emit (i.e. print) a key-value pair containing the
    #district (not state) and Aadhaar generated, separated by a tab.
    #Skip rows without the correct number of tokens and also skip
    #the header row.

    #You can see a copy of the the input Aadhaar data
    #in the link below:
    #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv

    #Since you are printing the output of your program, printing a debug
    #statement will interfere with the operation of the grader. Instead,
    #use the logging module, which we've configured to log to a file printed
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.

    for line in sys.stdin:
        # Dirty check so we doint evaluate a header line
        if "Registrar" in line:
            continue

        data = line.split(",")
        district = data[DISTRICT_INDEX]
        aadhaar_generated = data[AADHAAR_GENERATED_INDEX]

        print "{0}\t{1}".format(district,aadhaar_generated)


mapper()
