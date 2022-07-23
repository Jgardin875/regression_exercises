#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import env
import wrangle1

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split


# In[ ]:








# In[3]:


df, train, validate, test = wrangle1.wrangle_zillow()


# In[4]:


df = train


# In[30]:


df.shape


# # c 
# Write a function named plot_variable_pairs that accepts a dataframe as input and plots all of the pairwise relationships along with the regression line for each pair.

# In[5]:


def plot_variable_pairs(df):
    return sns.pairplot(df.sample(5000), diag_kind = 'kde', kind = 'reg', corner=True)


# In[6]:


plot_variable_pairs(train)


# In[ ]:





# In[ ]:





# # d
# Write a function named plot_categorical_and_continuous_vars that accepts your dataframe and the name of the columns that hold the continuous and categorical features and outputs 3 different plots for visualizing a categorical variable and a continuous variable.

# In[7]:


df.rename(columns = {'bedroomcnt': 'bed', 'bathroomcnt': 'bath', 'calculatedfinishedsquarefeet' : 'sqft',
   'taxvaluedollarcnt': 'tax_value'}, inplace = True)


# In[8]:


cat_col = list(df[['bed', 'bath', 'yearbuilt', 'fips']])


# In[9]:


cat_col


# In[10]:


cont_col = list(df[['sqft']])
cont_col






# In[18]:

# In[19]:


plt.figure(figsize=(16, 3))

for i, col in enumerate(cat_col):

    # i starts at 0, but plot nos should start at 1
    plot_number = i + 1

    l= len(cat_col)

    plt.subplot(1,l,plot_number)

    # Title with column name.
    plt.title(col)

    sns.barplot(x = df.groupby(col).tax_value.mean().index, y = df.groupby(col).tax_value.mean().values,)


# In[20]:



# In[21]:



# In[22]:


def plot_categorical_and_continuous_vars(df, cat_col, cont_col):

    plt.figure(figsize=(16, 3))

    for i, col in enumerate(cat_col):

        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1

        l= len(cat_col)

        plt.subplot(1,l,plot_number)

        # Title with column name.
        plt.title(col)

        sns.barplot(x = df.groupby(col).tax_value.mean().index, y = df.groupby(col).tax_value.mean().values)


# In[23]:


plot_categorical_and_continuous_vars(df, cat_col, cont_col)


# In[24]:



# In[48]:


def plot_categorical_and_continuous_vars(df, cat_col, cont_col):

    for i, col in enumerate(cat_col):
        plt.figure(figsize=(16, 3))
        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1

        l= len(cat_col)

        plt.subplot(1,l,plot_number)

        # Title with column name.
        plt.title(col)
        
        sns.stripplot(x = df[col], y = df.tax_value)
        #--------------------------------------------------------------
        plt.figure(figsize=(16, 3))
        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1

        l= len(cat_col)

        plt.subplot(1,l,plot_number)

        # Title with column name.
        plt.title(col)
        
        sns.boxplot(df[col], y = df.tax_value)
        
        #--------------------------------------------------------------
        plt.figure(figsize=(16, 3))
        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1

        l= len(cat_col)

        plt.subplot(1,l,plot_number)

        # Title with column name.
        plt.title(col)
        
        sns.barplot(df[col], y = df.tax_value)


# In[49]:


plot_categorical_and_continuous_vars(df, cat_col, cont_col)


# In[ ]:


# need to be pickier about outliers


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




