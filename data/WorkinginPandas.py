import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
Jenn Hubert
I did not include the data I collected in this project because I was nearly finished by the time I received it.
'''

'''
Below I am reading in the data in file 'a'. I have to re-order the columns.
At this time I notice that there is no gender attached so I may not use this data later on.
'''
df1=pd.read_csv('data/halloween2019a.csv', sep=(','))
#print("df1")
df1=df1.drop(['MiddleName'], axis=1)
df1['Name'] = df1['FirstName'] + ' ' + df1['LastName']
df1=df1.drop(['FirstName'], axis=1)
df1=df1.drop(['LastName'], axis=1)
df1 = df1.reindex(columns=['Name', 'DOB', 'DOD'])
#print(df1)
'''
Below I am reading in the data for the 'b' file and readying it to merge
'''
df2=pd.read_csv('data/halloween2019b.csv', sep=(','))
#print("df2")
df2['Name'] = df2['FirstName']+ " " + df2[' LastName']
df2=df2.drop(['FirstName'], axis=1)
df2=df2.drop([' LastName'], axis=1)
df2 = df2.reindex(columns=['Name', ' DOB', ' DOD', ' Sex'])
'''
Below I am renaming the column names because they have extra spaces.
'''
df2 = df2.rename(columns={' DOB': 'DOB', ' DOD': 'DOD', ' Sex': 'Sex'})
#print(df2)
'''
Below I am reading the data for file 'c' in. There isn't much cleaning to do before I merge it with the rest.
'''
df3=pd.read_csv('data/halloween2019c.csv', sep=(','))
#print("df3")
#print(df3)

'''
Below I am merging the dataframes into one dataframes. 
'''
newdf = pd.concat([df2, df3])
#print(newdf)
newdf2 = pd.concat([newdf, df1])

#print(newdf2)
'''
#Below I am dropping the rows that are missing any values and cleaning the Sex column.
'''
newdf2 = newdf2.dropna()
newdf2['Sex'] = newdf2['Sex'].replace([' m', ' f', 'm', 'f', 'F', 'M', 'male', 'female'], ['Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female'])
print(newdf2["Sex"])
'''
Below I am converting the dates to datetime formats.
'''
newdf2['DOD'] = pd.to_datetime(newdf2['DOD'], infer_datetime_format=True)
#print(newdf2["DOD"])
newdf2['DOB'] = pd.to_datetime(newdf2['DOB'], infer_datetime_format=True)
#print(newdf2["DOB"])
'''
I am finding life spans below.
'''
newdf2['DifferenceinDays'] = (newdf2['DOD'] - newdf2['DOB']).dt.days
newdf2['LifeSpan'] = (newdf2['DifferenceinDays'] / 365)
newdf2['LifeSpan']=newdf2["LifeSpan"].round()

newdf2=newdf2.drop(['DifferenceinDays'], axis=1)

#print(newdf2)

q3, q1 = np.percentile(newdf2['LifeSpan'], [75 ,25])
iqr = q3 - q1
print(iqr)

    
#plt.boxplot(newdf2['LifeSpan'])
#plt.show()
'''
The above boxplot shows that there are some people with negative life spans. I will delete their rows below as outliers.
'''
newdf2.drop(newdf2[newdf2['LifeSpan'] < 0 ].index, inplace=True)

'''
The below boxplot confirms I got rid of the records I wanted to.
'''
#plt.boxplot(newdf2['LifeSpan'])
#plt.show()


'''
I found the mean and median of life span regardless of Sex below

median=newdf2['LifeSpan'].median()
print("The median age is: ")
print(median)

mean=newdf2['LifeSpan'].mean()
mean=mean.round(0)
print("The mean age is: ")
print(mean)

I had to convert the datetime again in order to use if for the plot
'''
newdf2['DOB1'] = newdf2['DOB'].dt.strftime('%Y')
print(newdf2['DOB1'])

mean_price_by_Sex = newdf2.pivot_table(
    values='LifeSpan',
    index='Sex',
    columns='DOB1',
    aggfunc='mean'
)
print(mean_price_by_Sex)

ax = mean_price_by_Sex.T.plot(kind='bar', ylabel='LifeSpan')
plt.show()
