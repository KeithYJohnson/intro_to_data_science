import csv
import pdb
import urllib2
import numpy


def do_stuff(element):
    arr = element.split(',')
    return len(arr)

def other_stuff(element):
    return len(element)

def fix_file(filename):
    response = urllib2.urlopen(filename)
    body = response.read().rstrip()

    arr = body.split(',')
    flattened_arr = []

    for thing in arr:
        new_arr = thing.split(',')
        for another_thing in new_arr:
            flattened_arr.append(another_thing)

    chunked_arr = [flattened_arr[x:x+8] for x in xrange(0, len(flattened_arr), 8)]
    numpy_chunked_array = numpy.asarray(chunked_arr)

    pdb.set_trace()
    numpy.savetxt('foo.csv', numpy_chunked_array, delimiter=",")


    #should be a set of 1
    # correctness_counts = set(map(do_stuff, flattened_arr))




def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt

    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file.

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775

    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the
    Instructor Notes below for more details on the task.

    In addition, here is a CSV reader/writer introductory tutorial:
    1

    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:

    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
    for name in filenames:
        fix_file(name)

fix_turnstile_data(["http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt"])
