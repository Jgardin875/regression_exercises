#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, QuantileTransformer

import env
import wrangle1


# In[3]:


df, train, validate, test = wrangle1.wrangle_zillow()


# In[5]:


# used class model, added comments to prove understanding


# In[6]:


def scale_data(train, validate, test):
    #pick which columns to scale
    scale_columns = ['bedroomcnt', 'bathroomcnt', 'calculatedfinishedsquarefeet']
    #make copy so that the original values are unaffected
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()
    #define test
    mms = MinMaxScaler()
    #fit test to train only 
    mms.fit(train[scale_columns])
    #copies and selected columns = Min-Max transformed data of same selected columns. Used original data for transform in the equation, but the changes are not permanent to the original dataset. if you pull it up it'll be fine
    train_scaled[scale_columns] = mms.transform(train[scale_columns])
    validate_scaled[scale_columns] = mms.transform(validate[scale_columns])
    test_scaled[scale_columns] = mms.transform(test[scale_columns])
    
    return train_scaled, validate_scaled, test_scaled


# In[7]:


train_s, validate_s, test_s = scale_data(train, validate, test)


# In[8]:


x_train_s = train_s.drop(columns=['taxvaluedollarcnt'])
y_train_s = train_s.taxvaluedollarcnt

x_validate_s = validate_s.drop(columns=['taxvaluedollarcnt'])
y_validate_s = validate_s.taxvaluedollarcnt

x_test_s = test_s.drop(columns=['taxvaluedollarcnt'])
y_test_s = test_s.taxvaluedollarcnt


# In[ ]:


# original


# In[10]:


train.head()


# In[ ]:


#transformed


# In[12]:


x_train_s.head()


# In[ ]:




