#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import env

from sklearn.model_selection import train_test_split


# In[1]:


print('df, train, validate, test = wrangle1.wrangle_zillow()')


# In[ ]:





# # 1 Acquire:
# bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, and fips 
# from the zillow database for all 'Single Family Residential' properties.
# 

# In[3]:


url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/zillow'


# In[4]:


def new_zillow_data():
    return pd.read_sql('''SELECT
    p.bedroomcnt,
    p.bathroomcnt,
    p.calculatedfinishedsquarefeet,
    p.taxvaluedollarcnt,
    p.yearbuilt,
    p.taxamount,
    p.fips 
FROM properties_2017 p
LEFT JOIN propertylandusetype t USING (propertylandusetypeid)
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


#df = new_zillow_data()


# In[6]:


#df.to_csv('zillow.csv')


# In[7]:


df = get_zillow_data()


# In[8]:


df


# In[ ]:





# 
# 
# # # 2 Prep
# Using your acquired Zillow data, walk through the summarization and cleaning steps in your wrangle.ipynb file like we did above. You may handle the missing values however you feel is appropriate and meaninful; remember to document your process and decisions using markdown and code commenting where helpful.
# 

# In[ ]:





# In[9]:


df.isnull().sum()


# In[10]:


df.shape


# In[11]:


def prep_zillow(df):
    #drop nulls
    df.dropna(subset = ['bedroomcnt', 'bathroomcnt', 'calculatedfinishedsquarefeet',
       'taxvaluedollarcnt', 'yearbuilt', 'taxamount', 'fips'], inplace = True) #lose 0.59% of data
    
    
    #deal with outliers
    df = df[df.bathroomcnt < 7]
    df = df[df.bedroomcnt < 7]
    df = df[df.taxamount < 25_000]
    df = df[df.calculatedfinishedsquarefeet < 20_000]
    
    df.drop(columns = 'taxamount', inplace = True)
    return df
    #total data loss from nulls and outliers: 2.5


# In[12]:


df = prep_zillow(df)


# In[13]:


df


# In[14]:


df.shape


# In[15]:


2152863-2100070


# In[16]:


52793/2152863


# In[17]:


#df.info()


# In[18]:


df.isna().mean()


# 
# #from class
# 
# #df = new_zillow_data();
# 
# df[df.isna().any(axis=1)]
# 
#  What's the percentage of nulls?
# df.isna().mean()
# 
# #see wrangle explore for how to address outliers. didn't want all those graphs to show up when I imported wrangle.py
# 
# 

# In[ ]:





# 
# # 3 
# Store all of the necessary functions to automate your process from acquiring the data to returning a cleaned dataframe witn no missing values in your wrangle.py file. Name your final function wrangle_zillow.
# 

# In[19]:


def split_zillow_data(df):

    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123)
    return train, validate, test


# In[ ]:





# In[20]:


def wrangle_zillow():
    df = get_zillow_data()
    df = prep_zillow(df)
    train, validate, test = split_zillow_data(df)
    return df, train, validate, test


# In[ ]:





# In[21]:


df, train, validate, test = wrangle_zillow()


# In[22]:


df.shape, train.shape, validate.shape, test.shape


# In[23]:


df.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




