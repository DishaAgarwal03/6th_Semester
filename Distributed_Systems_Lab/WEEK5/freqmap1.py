# MapReduce program to find frequent words
# A basic mapper function/program that
# takes whatever is passed on the input and
# outputs tuples of all the words formatted
# as (word, 1)


from __future__ import print_function

# # for .csv
# import sys
# for line in sys.stdin:
#     L = [ (word.strip().lower(), 1 ) for word in line.strip().split(',') ]  # added ',' in split for csv
#     for word, n in L:
#         print( '%s\t%d' % (word, n) )

# for .xlsx  
import pandas as pd
df = pd.read_excel('German_Credit.xlsx')
for _, row in df.iterrows():
    line = ", ".join([str(value) for value in row.values])
    words = line.split(',')
    for word in words:
        print("%s\t%s" % (word, 1))
        
        
