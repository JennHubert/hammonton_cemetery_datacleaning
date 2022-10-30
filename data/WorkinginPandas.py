from turtle import right
import pandas as pd
from functools import reduce
import numpy as np

'''
Jenn Hubert
'''

'''
Below I am reading in the data in file 'a'. I have to re-order the columns.
At this time I notice that there is no gender attached so I may not use this data later on.
'''
df1=pd.read_csv('data/halloween2019a.csv', sep=(','))
print("df1")
df1=df1.drop(['MiddleName'], axis=1)
df1['Name'] = df1['FirstName'] + ' ' + df1['LastName']
df1=df1.drop(['FirstName'], axis=1)
df1=df1.drop(['LastName'], axis=1)
df1 = df1.reindex(columns=['Name', 'DOB', 'DOD'])
print(df1)
'''
Below I am reading in the data for the 'b' file and readying it to merge
'''
df2=pd.read_csv('data/halloween2019b.csv', sep=(','))
print("df2")
df2['Name'] = df2['FirstName']+ " " + df2[' LastName']
df2=df2.drop(['FirstName'], axis=1)
df2=df2.drop([' LastName'], axis=1)
df2 = df2.reindex(columns=['Name', ' DOB', ' DOD', ' Sex'])
'''
Below I am renaming the column names because they have extra spaces.
'''
df2 = df2.rename(columns={' DOB': 'DOB', ' DOD': 'DOD', ' Sex': 'Sex'})
print(df2)

'''
Below I am reading the data for file 'c' in. There isn't much cleaning to do before I merge it with the rest.
'''
df3=pd.read_csv('data/halloween2019c.csv', sep=(','))
print("df3")
print(df3)
print("COMPLETED")

'''
Below I am merging the dataframes into one dataframes. 
I have chosen to leave the data in df1 behind because there is not sex attached to each record
'''
newdf = pd.concat([df2, df3])
print(newdf)

newdf2 = pd.concat([newdf, df1])
print(newdf2)
#newdf["Sex"].replace("f", "Female", regex=True)
#print(newdf["Sex"])


