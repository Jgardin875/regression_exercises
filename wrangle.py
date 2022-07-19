#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import env


# new_zillow_data() \
# get_zillow_data() \
# prep_zillow() \
# wrangle_zillow()
# 

# # 1 Acquire:
# 
# bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, and fips 
# 
# from the zillow database for all 'Single Family Residential' properties.

# In[2]:


url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/zillow'


# In[3]:


def new_zillow_data():
    return pd.read_sql('''SELECT
    p.bedroomcnt,
    p.bathroomcnt,
    p.calculatedfinishedsquarefeet,
    p.taxvaluedollarcnt,
    p.yearbuilt,
    p.taxamount,
    p.fips,
    t.propertylandusedesc
FROM properties_2017 p
JOIN propertylandusetype t USING (propertylandusetypeid)
WHERE t.propertylandusedesc = 'Single Family Residential'
''', url)


# # 1 Answer

# In[4]:


def new_zillow_data():
    return pd.read_sql('''SELECT
    p.bedroomcnt,
    p.bathroomcnt,
    p.calculatedfinishedsquarefeet,
    p.taxvaluedollarcnt,
    p.yearbuilt,
    p.taxamount,
    p.fips,
    t.propertylandusedesc
FROM properties_2017 p
JOIN propertylandusetype t USING (propertylandusetypeid)
WHERE t.propertylandusedesc = 'Single Family Residential'
''', url)


import os

def get_zillow_data():
    filename = "zillow.csv"
    
    # if file is available locally, read it
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col = 0)
    
    # if file not available locally, acquire data from SQL database
    # and write it as csv locally for future use
    else:
        # read the SQL query into a dataframe
        df_zillow = new_zillow_data()
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df_zillow.to_csv(filename)

        # Return the dataframe to the calling code
        return df_zillow


# In[5]:


df = get_zillow_data()


# # 2 Prep
# 
# Using your acquired Zillow data, walk through the summarization and cleaning steps in your wrangle.ipynb file like we did above. You may handle the missing values however you feel is appropriate and meaninful; remember to document your process and decisions using markdown and code commenting where helpful.
# 

# In[6]:


# df.info()

#i checked it here in my original code. 
#But to prevent it from popping up whenver I import wrangle 
#I commeted out after verifying it worked


# In[7]:


df.shape


# In[8]:


df.describe().round(2)


# In[9]:


df.isnull().sum()


# In[10]:


df_drop = df


# In[11]:


df_drop.shape


# In[12]:


df_drop.dropna(subset=['yearbuilt'], inplace = True)


# In[13]:


df_drop.dropna(subset=['taxamount'], inplace = True)


# In[14]:


df_drop.dropna(subset=['calculatedfinishedsquarefeet'], inplace = True)


# In[15]:


df_drop.isnull().sum()


# In[16]:


df_drop.dropna(subset=['taxvaluedollarcnt'], inplace = True)


# In[17]:


df.shape


# In[18]:


df_drop.isnull().sum()


# In[19]:


df_drop.shape


# In[20]:


# if I drop all the null values:
dropped = 9337 +2708 +565 +18


# In[21]:


dropped/df.shape[0]


# In[22]:


# i lose ~0.6% of the data

#i'm okay with that


# In[23]:



df.shape


# In[24]:


df.dropna(inplace = True)


# In[25]:


df.shape


# In[ ]:





# # 2 Answer

# In[33]:


def prep_zillow(df):
    #drop nulls
    df.dropna(inplace = True) #lose 0.59% of data
    
    #drop extra columns-this column is teh single family residence filter
    df = df.drop(columns = 'propertylandusedesc')
    
    #deal with outliers
    df = df[df.bathroomcnt < 7]
    df = df[df.bedroomcnt < 7]
    df = df[df.taxamount < 25_000]
    df = df[df.calculatedfinishedsquarefeet < 20_000] 
    #total data loss from nulls and outliers: 3.2%
    return


# In[ ]:





# In[ ]:


#from class


# In[ ]:


#df = new_zillow_data();


# In[31]:


df[df.isna().any(axis=1)]


# In[ ]:


# What's the percentage of nulls?
df.isna().mean()


# In[ ]:


#see wrangle explore for how to address outliers. didn't want all those graphs to show up when I imported wrangle.py


# In[ ]:


# address outliers


# In[ ]:


df.columns.tolist()


# In[ ]:


for column in df.columns:
    print(column)
    print(df[column].value_counts())
    print("-----------------")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 3 
# Store all of the necessary functions to automate your process from acquiring the data to returning a cleaned dataframe witn no missing values in your wrangle.py file. Name your final function wrangle_zillow.

# In[34]:


def wrangle_zillow():
    df = get_zillow_data()
    prep_zillow(df)
    return df


# In[35]:


df = wrangle_zillow()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




