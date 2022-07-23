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





# In[ ]:





# Exercises
# 
# Our Zillow scenario continues:
# 
# As a Codeup data science graduate, you want to show off your skills to the Zillow data science team in hopes of getting an interview for a position you saw pop up on LinkedIn. You thought it might look impressive to build an end-to-end project in which you use some of their Kaggle data to predict property values using some of their available features; who knows, you might even do some feature engineering to blow them away. Your goal is to predict the values of single unit properties using the observations from 2017.
# 
# In these exercises, you will run through the stages of exploration as you continue to work toward the above goal.
# 
#     As with encoded vs. unencoded data, we recommend exploring un-scaled data in your EDA process.
# 
#     Make sure to perform a train, validate, test split before and use only your train dataset to explore the relationships between independent variables with other independent variables or independent variables with your target variable.
# 
#     Write a function named plot_variable_pairs that accepts a dataframe as input and plots all of the pairwise relationships along with the regression line for each pair.
# 
#     Write a function named plot_categorical_and_continuous_vars that accepts your dataframe and the name of the columns that hold the continuous and categorical features and outputs 3 different plots for visualizing a categorical variable and a continuous variable.
# 
#     Save the functions you have written to create visualizations in your explore.py file. Rewrite your notebook code so that you are using the functions imported from this file.
# 
#     Use the functions you created above to explore your Zillow train dataset in your explore.ipynb notebook.
# 
#     Come up with some initial hypotheses based on your goal of predicting property value.
# 
#     Visualize all combinations of variables in some way.
# 
#     Run the appropriate statistical tests where needed.
# 
#     What independent variables are correlated with the dependent variable, home value?
# 
#     Which independent variables are correlated with other independent variables (bedrooms, bathrooms, year built, square feet)?
# 
#     Make sure to document your takeaways from visualizations and statistical tests as well as the decisions you make throughout your process.
# 
#     Explore your dataset with any other visualizations you think will be helpful.
# 

# In[2]:


# a, b


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


# In[11]:


cont_targ = df.tax_value


# In[12]:


df.head()


# In[13]:


df.yearbuilt.min()


# In[14]:


df.yearbuilt.max()


# In[15]:


year_bins = pd.cut(df.yearbuilt, bins = 5)


# In[16]:


l = pd.DataFrame(year_bins.value_counts())
l


# In[17]:


df.groupby('yearbuilt').tax_value.mean()


# In[18]:


sns.barplot(x = df.groupby('bed').tax_value.mean().index, y = df.groupby('bed').tax_value.mean().values,)


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


df.bath.value_counts(sort = False).sort_index()


# In[21]:


cont_targ


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


df


# In[ ]:





# In[25]:


#continous


# In[ ]:





# In[26]:


sns.scatterplot(x = df.sqft, y =  df.tax_value)


# In[ ]:





# In[44]:


sns.stripplot(x = df.bed, y = df.tax_value)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





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





# # 5

# Save the functions you have written to create visualizations in your explore.py file. Rewrite your notebook code so that you are using the functions imported from this file.

# In[ ]:





# # 6

# Use the functions you created above to explore your Zillow train dataset in your explore.ipynb notebook.

# In[ ]:


#literally just did that


# In[ ]:





# 
# 
# # 7
# 
# Come up with some initial hypotheses based on your goal of predicting property value.
# 
#     - target variable trends nicely with beds, bath, 
#     - I think trends in sqrft 
# 
# 
# # 8
# Visualize all combinations of variables in some way.
# 
# Run the appropriate statistical tests where needed.
# 
# What independent variables are correlated with the dependent variable, home value?
# 
# Which independent variables are correlated with other independent variables (bedrooms, bathrooms, year built, square feet)?
# 
# Make sure to document your takeaways from visualizations and statistical tests as well as the decisions you make throughout your process.
# 
# Explore your dataset with any other visualizations you think will be helpful.
# 

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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Fellow student's work, I thought was super cool 
# 
# # NOT MY WORK

# In[29]:


def plot_categorical_and_continuous_vars_josh(df, categorical_cols, continuous_cols):
    """Spits out a bunch of plots to speed up exploration."""
    # Save ourselves some time on huge datasets
    if len(df) > 100_000:
        df = df.sample(100_000)
    
    # Some quickmaths to determine each figure size.
    units = 4
    width = 3*units
    height = len(categorical_cols)*units-1

    # Make a new subplots figure for each continuous variable
    for con in continuous_cols:
        fig, ax = plt.subplots(nrows=len(categorical_cols), ncols=3, figsize=(width,height))

        # Make a row consisting of a bar, box, and violin plot for each categorical variable
        for row, cat in enumerate(categorical_cols):
            # For readability, get a sorted list of each categorical bucket
            sort_order = df[cat].sort_values().unique().tolist()

            plot1 = sns.barplot(data=df, x=cat, y=con, ax=ax[row][0], order=sort_order)
            plot1.set_ylabel(cat)   # Only the leftmost plot gets a ylabel, labeling the entire row (not the y axis!)
            plot1.set_xlabel(None)  # Remove the xlabel, that goes in the ylabel
            # Rotate xtick labels so that they can't overlap each other.
            for item in plot1.get_xticklabels():
                item.set_rotation(90)
            
            plot2 = sns.boxplot(data=df, x=cat, y=con, ax=ax[row][1], order=sort_order)
            plot2.set_ylabel(None)
            plot2.set_xlabel(None)
            for item in plot2.get_xticklabels():
                item.set_rotation(90)
            
            plot3 = sns.violinplot(data=df, x=cat, y=con, ax=ax[row][2], order=sort_order)
            plot3.set_ylabel(None)
            plot3.set_xlabel(None)
            for item in plot3.get_xticklabels():
                item.set_rotation(90)
        # Title the figure with the continuous variable so we know what we are looking at.
        fig.suptitle(con)


# # RETURN TO MY WORK

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





# In[ ]:




