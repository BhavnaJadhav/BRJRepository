#!/usr/bin/env python
# coding: utf-8

# In[339]:


import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns
import numpy as np
import pandas as pd
import os 

#Importing map of rainfall distribution across India
India = np.array(Image.open('E:\Software\Anaconda\Rain_data\Annual-mean-rainfall-map-of-India.jpg'))
fig=plt.figure(figsize=(8,8))
plt.imshow(India)
plt.axis('off')
#plt.ioff()
plt.show()


# In[66]:


#Importing the 117 years of Indian rainfall data , source data.gov.in 
df= pd.read_csv("E:\Software\Anaconda\Rain_data\Sub_Division_IMD_2017.csv")
df.head()
#describe(df)


# In[340]:


df.info()                                                      # Type of values in the data set


# In[342]:


# # Summary of dataset
print('Rows     :',df.shape[0])
print('Columns  :',df.shape[1])
print('\nFeatures :\n     :',df.columns.tolist())
print('\nMissing values    :',df.isnull().values.sum())
print('\nUnique values :  \n',df.nunique())


# In[61]:


# Inspecting data for null values 
total = df.isnull().sum().sort_values(ascending = False)
percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)*100
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
print(df.isnull().sum())


# In[54]:


#Inspecting the data
f, ax = plt.subplots(figsize=(15, 6))
plt.xticks(rotation='90')
sns.barplot(x=missing_data.index, y=missing_data['Percent'])
plt.xlabel('Features', fontsize=15)
plt.ylabel('Percent of missing values', fontsize=15)
plt.title('Percent missing data by feature', fontsize=15)
missing_data.head()


# In[67]:


df.describe()


# In[69]:


#Replacing the missing values with mean of the column
df['JAN'].fillna((df['JAN'].mean()),inplace = True)
df['FEB'].fillna((df['FEB'].mean()),inplace = True)
df['MAR'].fillna((df['MAR'].mean()),inplace = True)
df['APR'].fillna((df['APR'].mean()),inplace = True)
df['MAY'].fillna((df['MAY'].mean()),inplace = True)
df['JUN'].fillna((df['JUN'].mean()),inplace = True)
df['JUL'].fillna((df['JUL'].mean()),inplace = True)
df['AUG'].fillna((df['AUG'].mean()),inplace = True)
df['SEP'].fillna((df['SEP'].mean()),inplace = True)
df['OCT'].fillna((df['OCT'].mean()),inplace = True)
df['NOV'].fillna((df['NOV'].mean()),inplace = True)
df['DEC'].fillna((df['DEC'].mean()),inplace = True)
df['ANNUAL'].fillna((df['ANNUAL'].mean()), inplace=True)
df['JF'].fillna((df['JF'].mean()), inplace=True)
df['MAM'].fillna((df['MAM'].mean()), inplace=True)
df['JJAS'].fillna((df['JJAS'].mean()), inplace=True)
df['OND'].fillna((df['OND'].mean()), inplace=True)


# In[72]:


df.head()


# In[75]:


df.describe().T


# In[161]:


# Annual rainfall in India
ax = df.groupby("YEAR").mean()['ANNUAL'].plot(ylim=(1000,1800),color = 'b',marker = 'o',linestyle='-',Linewidth =2,figsize=(14,9));
df['MA10'] = df.groupby('YEAR').mean()['ANNUAL'].rolling(10).mean()
df.MA10.plot(color='r',linewidth =4)
plt.xlabel('Year' ,fontsize =20,fontstyle ='italic')
plt.ylabel('Annual Rain (in mm)',fontsize = 20,fontstyle='italic')
plt.title('Annual Rainfall in India from Year 1901 to 2017',fontsize=22,fontstyle = 'italic')
ax.tick_params(labelsize =10)
plt.grid()
plt.ioff()                                                          # interactive mode off


# In[247]:


#Seasonal rainfall in India
df[['YEAR','JF','MAM','JJAS','OND']].groupby("YEAR").mean().plot(figsize=(13,8),color=('m','r','c','b'));
plt.xlabel('Year',fontsize=15)
plt.ylabel('Seasonal Rainfall (in mm)',fontsize=15,fontstyle ='italic')
plt.title('Seasonal Rainfall from Year 1901 to 2017',fontsize=20,fontstyle ='italic')
ax.tick_params(labelsize=10)
plt.grid()
# # plt.ioff()


# In[328]:


#Season wise rainfall in India
df[['SUBDIVISION','JF','MAM','JJAS','OND']].groupby("SUBDIVISION").mean().sort_values('JJAS' ,ascending = False).plot.bar(width=0.5,edgecolor='k',align='center',stacked=True,figsize=(16,8));

plt.xlabel('Subdivision',fontsize=30)
plt.ylabel('Rainfall (in mm)',fontsize=20)
plt.title('Rainfall in Subdivisions of India',fontsize=25)
ax.tick_params(labelsize=15)
plt.grid()
plt.ioff()


# In[330]:


# fig = plt.figure(figsize=(16,8))
# ax = fig.add_subplot(111)
df.groupby('SUBDIVISION').mean().sort_values(by='ANNUAL', ascending=False)['ANNUAL'].plot(kind = 'bar', color='b',width=0.65,linewidth=3,edgecolor='k',align='center',title='Subdivision wise Average Annual Rainfall', fontsize=20)
plt.xticks(rotation = 90)
plt.ylabel('Average Annual Rainfall (in mm)')
ax.title.set_fontsize(60)
ax.xaxis.label.set_fontsize(20)
ax.yaxis.label.set_fontsize(20)
#print(df.groupby('SUBDIVISION').mean().sort_values(by='ANNUAL', ascending=False)['ANNUAL'][[0,1,2]])               #max 3 
#print(df.groupby('SUBDIVISION').mean().sort_values(by='ANNUAL', ascending=False)['ANNUAL'][[33,34,35]])            #min 3


# In[331]:


#Box Plot of Annual Rainfall
plt.rcParams['figure.figsize']=(23,10)
ax = sns.boxplot(x="SUBDIVISION", y="ANNUAL", data=df,width=0.8,linewidth=3)
ax.set_xlabel('Subdivision',fontsize=25)
ax.set_ylabel('Annual Rainfall (in mm)',fontsize=25)
plt.title('Annual Rainfall in Subdivisions of India',fontsize=30)
ax.tick_params(axis='x',labelsize=20,rotation=90)
ax.tick_params(axis='y',labelsize=20,rotation=0)
plt.grid()
plt.ioff()


# In[327]:


#Monthwise Rainfall in India
df[['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']].mean().plot.bar(width=0.5,edgecolor='k',align='center',linewidth=2,figsize=(16,8),
                                                                                                 color=('y','b','g','r','brown','y','pink','m','c','brown','r','b') )
plt.xlabel('Month',fontsize = 15,fontstyle = 'italic',color = 'b')
plt.ylabel('Monthwise Rainfall in (mm)',fontsize = 15,fontstyle = 'italic',color = 'b')
plt.title('Monthwise Rainfall in India',fontsize = 22,fontstyle = 'italic',color = 'b')
ax.tick_params(labelsize=20)
plt.grid()
#plt.ioff()


# In[311]:


#Heat Map of Rainfall
fig=plt.gcf()                                                             #Get Current Figure. plt. gcf() allows you to get a reference to the current figure when using pyplot.
fig.set_size_inches(15,15)
fig=sns.heatmap(df.corr(),annot=True,cmap='summer',linewidths=1,linecolor='k',square=True,mask=False, vmin=-1, vmax=1,cbar_kws={"orientation": "vertical"},cbar=True)


# In[ ]:


We can see that Annual rainfall has very high correlation to the rainfall received in the months of Jun-Sep


# In[ ]:




