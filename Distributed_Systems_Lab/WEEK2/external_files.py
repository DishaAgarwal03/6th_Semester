import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading a CSV file & XLS file format
df = pd.read_csv('xyz.csv',header=None)
print(df.head()) # This will display 1 st 5 records
print(df.tail()) # This will display last 5 records
# The above dataset doesn't have header, we shall attach our own header.
df.columns=['preg','glu','bp','sft','ins','bmi','dpf','age','class']
#Let us visualize the scatter plot of two continuous variable.
plt.scatter(df['bmi'],df['glu'])
plt.xlabel('bmi')
plt.ylabel('Glucose')
plt.show()
#Let us visualize the histogram of another continuous variable 'Age'
plt.hist(df['age'])
plt.show()
#Let us visualize the distribution 'Age' with respect to Categories: Label-O(Healthy), Label-1 (Diabetes)
#We can observe the median age of diabetes is slightly greater than median age of healthy
print("---------------------------------------------------------------------")

W = pd.read_csv('xyz.xls',header=None)
print(W.head()) # XLS file format also, we can read using pd.read_csv
D= np.loadtxt('xyz.txt',delimiter=",")
print(D[:5,:]) # this file is loaded in Numpy 2D array format
print("---------------------------------------------------------------------")

# Reading a XLSX file format
G=pd.read_excel('xyz.xlsx',sheet_name='Sheet1')
print(G.head())
# Here additionally we need to pass the sheet_name. If not specified, it will read the first page by default.
print("---------------------------------------------------------------------")

# Reading a HTML file format
# Pandas can read table tabs off of html. For example:
B = pd.read_html('xyz.html')
print(B)
print("---------------------------------------------------------------------")

# Reading a TXT file format
H = pd.read_table('HR.txt')
print(H.head())
f=H['Department'].value_counts()
print(f)
print("---------------------------------------------------------------------")

#We can visualize the distribution of categorical values using
# bar plot and pie chart
f.plot(kind='bar')
plt.show()
# The above bar plot can be perceived in terms of Pie chart
# which would give % percentage information
f.plot(kind='pie') 
plt.show()
#We can visualize two categorical variables at a time
fa=pd.crosstab(H['Gender'],H['Attrition'])
fa.plot(kind='bar')
plt.show()
