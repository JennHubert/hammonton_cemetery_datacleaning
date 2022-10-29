import pandas as pd
import glob
import os

'''
Jenn Hubert
'''
'''
file1 ='data/halloween2019a.csv'
file2 ='data/halloween2019b.csv'
file3 ='data/halloween2019c.csv'
print("hi")
df = pd.concat(
    map(pd.read_csv([file1, file2, file3])))
print(df.head())
'''
'''
files = os.path.join("data", "halloween2019*.csv")
                     
files = glob.glob(files)

df = pd.concat(map(pd.read_csv, files), ignore_index=True)
'''
df1=pd.read_csv('data/halloween2019a.csv', sep=(','))
print("df1")
df1=df1.drop(['MiddleName'], axis=1)
df1['Name'] = df1['FirstName'] + ' ' + df1['LastName']
df1=df1.drop(['FirstName'], axis=1)
df1=df1.drop(['LastName'], axis=1)
df1 = df1.reindex(columns=['Name', 'DOB', 'DOD'])
print(df1)

df2=pd.read_csv('data/halloween2019b.csv', sep=(','))
print("df2")
for col in df2.columns:
    print(col)
df2['Name'] = df2['FirstName']+ " " + df2[' LastName']
df2=df2.drop(['FirstName'], axis=1)
df2=df2.drop([' LastName'], axis=1)
df2 = df2.reindex(columns=['Name', ' DOB', ' DOD', ' Sex'])
print(df2)

df3=pd.read_csv('data/halloween2019c.csv', sep=(','))
print("df3")
print(df3)



print("COMPLETED")
print(df1)
print(df2)
print(df3)
#df = pd.merge(df1, df2, df3)
#print(df)
