import pandas as pd
import numpy as np
s=pd.Series([3,9,-2,10,5])
print(s.sum())
print(s.min())
print(s.max())
print("---------------------------------------------------------------")


# Creating a Data Frame
data = [['Dinesh',10],['Nithya',12],['Raji',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)
print("---------------------------------------------------------------")


# Indexed Data Frame
data = {'Name':['Kavitha', 'Sudha', 'Raju','Vignesh'],'Age':[28,34,29,42]}
df1 = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df1)
print("---------------------------------------------------------------")


# Creating a DataFrame using Dictionary
df2=pd.DataFrame({'A':pd.Timestamp('20130102'),'B':np.array([3]*4,dtype='int32'),
'C':pd.Categorical(['Male','Female','Male','Female'])})
print(df2.shape)
print(df2.dtypes)
print(df2.head())  #will display first 5 records
print(df2.tail() ) #will display last 5 records
print(df.describe())
print(df.T ) # will transpose the data frame
print("---------------------------------------------------------------")


dates=pd.date_range('20130101', periods=100)
df = pd.DataFrame(np.random.randn(100,4), index=dates, columns=list('ABCD'))
# To view first 5 records
print(df.head())
# To view last 5 records
print(df.tail())
# To view the index
print(df.index)
# To view the column names
print(df.columns)
# To transpose the df
print(df.T)
# Sorting by Axis
print(df.sort_index(axis=1, ascending=False))
# Sorting by Values
print(df.sort_values(by='B'))
# Slicing the rows
print(df[0:3]) # which slice first 3 records (rows)
# Slicing with index name
print(df['20130105':'20130110'])
# Slicing with row and column index (like 2D Matrix)
print(df.iloc[0])  # will fetch entire 1 st row
print(df.iloc[0,:2] ) # will fetch 1 st row, first 2 columns
print(df.iloc[0,0])  # will fetch 1 st row, 1 st column element (single element)
# Selecting a single column
print(df['A']) #which yields a Series
# Selecting more than one column
print(df[['A','B']]) #entire 2 columns
# Selecting more than one column, with selected number of records
print(df[['A','B']][:5] )#first 5 records
# [OR]
print(df.loc['20130101':'20130105',['A','B']][:5] ) # first 5 records
print("---------------------------------------------------------------")
       

# Boolean Indexing
df = pd.DataFrame(np.random.randn(6,4), columns=list('ABCD'))
print(df[df.A>0])
# Include a 6 th column (a categorical) character data
df['F']=['Male','Female','Female','Male','Female','Female']
# Setting by assigning with a numpy array
df.loc[:,'D']=np.array([5]*len(df))
# Which will replace the 'D', column with all 5
print(df)

# Deleting a row or column
df.drop ('A', axis =1, inplace=True)
print(df)
# will drop the column name specified in col_name
df.drop (3, axis =0, inplace=True)
print(df)
# will drop the row specified in row_index
print("---------------------------------------------------------------")


# Concatenation of two Data Frames
# Let df1 be of size 10 x 5 and df2 of size 10 x 3 if concatenated horizontally (as a new column
# insertion)
df1 = pd.DataFrame(index=range(10),columns=range(5))
df2 = pd.DataFrame(index=range(10),columns=range(3))
Df_new= pd.concat ([df1, df2], axis=1)
print(Df_new.shape)

# Let A dataframe of size 10 x 5 and B dataframe of size 15 x 5 if concatenated Vertically (as a
# new row insertion)
A = pd.DataFrame(np.random.randn(10,5),columns=list('ABCDE'))
B = pd.DataFrame(index=range(15),columns=range(5))
D = pd.concat ([A, B], axis=0)
print(D.shape)
# ** Sorting and Ordering a DataFrame:**
# For the given DataFrame let us sort the age column
# Let the dataframe be “A”
print(A.sort_values(by = 'A'))
print("---------------------------------------------------------------")
