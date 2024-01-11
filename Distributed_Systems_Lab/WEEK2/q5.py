# 15. a) Create two data frames df1 and df2. df1 contains one column ‘Name’ and df2 contains 4 columns ‘Maths’,
# ‘Physics’, ‘Chemistry’ and ‘Biology’ .
# b) Concatenate two data frames df1 and df2. Now insert one column ‘Total’ to the new data frame df_new
# and find the sum of all marks.
import pandas as pd

df1 = pd.DataFrame({'Name': ['A', 'B']})
df2 = pd.DataFrame({'Maths': [80, 75],
                    'Physics': [85, 70],
                    'Chemistry': [90, 65],
                    'Biology': [95, 80]})

df_new = pd.concat([df1, df2], axis=1)
df_new['Total'] = df_new.sum(axis=1, numeric_only=True)
print(df_new)
