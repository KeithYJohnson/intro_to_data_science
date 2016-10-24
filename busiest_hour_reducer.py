import sys
import logging
# import itertools

# from util import reducer_logfile
# logging.basicConfig(filename=reducer_logfile, format='%(message)s',
#                     level=logging.INFO, filemode='w')

def reducer():
    '''
    Write a reducer that will compute the busiest date and time (that is, the
    date and time with the most entries) for each turnstile unit. Ties should
    be broken in favor of datetimes that are later on in the month of May. You
    may assume that the contents of the reducer will be sorted so that all entries
    corresponding to a given UNIT will be grouped together.

    The reducer should print its output with the UNIT name, the datetime (which
    is the DATEn followed by the TIMEn column, separated by a single space), and
    the number of entries at this datetime, separated by tabs.

    For example, the output of the reducer should look like this:
    R001    2011-05-11 17:00:00	   31213.0
    R002	2011-05-12 21:00:00	   4295.0
    R003	2011-05-05 12:00:00	   995.0
    R004	2011-05-12 12:00:00	   2318.0
    R005	2011-05-10 12:00:00	   2705.0
    R006	2011-05-25 12:00:00	   2784.0
    R007	2011-05-10 12:00:00	   1763.0
    R008	2011-05-12 12:00:00	   1724.0
    R009	2011-05-05 12:00:00	   1230.0
    R010	2011-05-09 18:00:00	   30916.0
    ...
    ...

    Since you are printing the output of your program, printing a debug
    statement will interfere with the operation of the grader. In,stead,
    use the logging module, which we've configured to log to a file printed
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''


    turnstile_unit_info = {}
    for line in sys.stdin:
        unit, entriesn_hourly, date_n, time_n = line.split("\t")
        entriesn_hourly = float(entriesn_hourly)

        if not unit and entriesn_hourly and date_n and time_n:
            continue

        if unit in turnstile_unit_info.keys():
            datetime = datetimestamp(date_n, time_n)
            turnstile_unit_info[unit].keys()
            if datetime in turnstile_unit_info[unit].keys():
                # This branch represents a double entry so probably a mistake?
                turnstile_unit_info[unit][datetime] += entriesn_hourly
            else:
                turnstile_unit_info[unit][datetime] = entriesn_hourly
        else:
            turnstile_unit_info[unit] = {}
            datetime = datetimestamp(date_n, time_n)

            if datetime in turnstile_unit_info[unit].keys():
                turnstile_unit_info[unit][datetime] += entriesn_hourly
            else:
                turnstile_unit_info[unit][datetime] = entriesn_hourly

    for unit in turnstile_unit_info.keys():
        busiest_hour = get_busiest_hour(unit,turnstile_unit_info)
        busiest_hours_entries = float(turnstile_unit_info[unit][busiest_hour])
        print '%s\t%s\t%f' % (unit, busiest_hour.rstrip(), busiest_hours_entries)


def datetimestamp(date, time):
    return  date + " " + time

def get_busiest_hour(unit, turnstile_unit_info):
    hours = turnstile_unit_info[unit]
    busiest_hour = max(hours, key=hours.get)

    keys_with_busiest_hour_value = []
    for key, value in hours.items():
        if value == hours[busiest_hour]:
            keys_with_busiest_hour_value.append(key)

    if len(keys_with_busiest_hour_value) > 0:
        sorted_datetimestamps = sorted(keys_with_busiest_hour_value)
        latest_datetimestamp = sorted_datetimestamps[-1]
        return latest_datetimestamp
    else:
        return busiest_hour

reducer()
