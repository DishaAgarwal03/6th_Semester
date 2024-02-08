# 3. MapReduce program to explore the dataset and perform the filtering (typically
# creating key/value pairs) by mapper and perform the count and summary
# operation on the instances.

import fileinput
transactions_count = 0
sales_total = 0
for line in fileinput.input():
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue
    current_key, current_value = data
    transactions_count += 1
    sales_total += float(current_value)
print (transactions_count, "\t", sales_total)