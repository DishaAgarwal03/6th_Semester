# Exercise 1: Try the above word count program for the Heart Disease dataset, covid_19_data
# dataset, example dataset and German Credit dataset

# for .csv
import sys
for line in sys.stdin:    
    line = line.strip() #IF DO NOT STRIP THEN LAST WORD MAY HAVE \t AND IT WON'T BE TAKEN INTO ACCOUNT BY REDUCER
    words = line.split(',')   # '\t' for .txt
    for word in words:
        print("%s,%s" %(word, 1))
        
# # for .xlsx  
# import pandas as pd
# df = pd.read_excel('German Credit.xlsx')
# # Iterate over the rows in the DataFrame and process each word
# for _, row in df.iterrows():
#     line = ", ".join([str(value) for value in row.values])
#     words = line.split(',')
#     for word in words:
#         print("%s,%s" % (word, 1))