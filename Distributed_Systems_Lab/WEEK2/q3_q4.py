# 13. Define a dictionary containing Students data {Name, Height, Qualification}.
# a) Convert the dictionary into DataFrame
# b) Declare a list that is to be converted into a new column (Address}
# c) Using 'Address' as the column name and equate it to the list and display the result.

# 14.
# Define a dictionary containing Students data {Name, Height, Qualification}.
# a) Convert the dictionary into DataFrame
# b) Use DataFrame.insert() to add a column and display the result.
import pandas as pd

data = {'Name':['Kavitha', 'Sudha', 'Raju','Vignesh'],'Height':[162,160,172,168],'Qualification':['12th','BTech','MTech','PhD']}
df = pd.DataFrame(data)
print(df)

l = ['F','F','M','M']
df['Gender'] = l
print(df)

df.insert(4, "City", ["New York", "London", "Paris", "Manipal"])
print(df)