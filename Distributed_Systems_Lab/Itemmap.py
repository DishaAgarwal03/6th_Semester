# 3. MapReduce program to explore the dataset and perform the filtering (typically
# creating key/value pairs) by mapper and perform the count and summary
# operation on the instances.

#import string
import fileinput
for line in fileinput.input():
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, location, item, cost, payment = data
        print ("{0}\t{1}".format(location, cost))