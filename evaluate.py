#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression 
from math import sqrt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

import env
import wrangle1


# In[16]:




def r2_setup(df, x_train, y_train):
    #set up model, predictions, baseline
    model = LinearRegression().fit(x_train, y_train)
    predictions = model.predict(x_train)
    baseline = y_train.mean()
   
    #set up columns for later
    df['yhat'] = predictions
    df['baseline'] = baseline

    # residual = actual - predicted
    df['residual'] = y_train - df.yhat
    df['baseline_residual'] = y_train - df.baseline
    
    #sq columns
    df['residual^2'] = df.residual**2
    df['baseline_residual^2'] = df.baseline_residual**2
    return df




def plot_residuals(y, yhat):
    residuals = yhat - y
    plt.scatter(x=y, y=residuals)
    plt.title('Residual plot')         

    
    
def regression_errors_mine(df):    
    SSE = df['residual^2'].sum()
    SSE_baseline = df['baseline_residual^2'].sum()
    print('SSE =', "{:.1f}".format(SSE))
    print("SSE Baseline =", "{:.1f}".format(SSE_baseline))

    #total sum of squares is teh SSE for baseline
    TSS = SSE_baseline

    # explained sum of squares
    ESS = TSS - SSE
    print('ESS =', "{:.1f}".format(ESS))
    
    #mean sqr
    MSE = SSE/len(df)
    MSE_baseline = SSE_baseline/len(df)
    print("MSE = ", "{:.1f}".format(MSE))
    print("MSE baseline = ", "{:.1f}".format(MSE_baseline))
    
    #root mean sqr
    RMSE = sqrt(MSE)
    RMSE_baseline =  sqrt(MSE_baseline)
    print("RMSE = ", "{:.1f}".format(RMSE))
    print("RMSE baseline = ", "{:.1f}".format(RMSE_baseline))
    return df


from sklearn.metrics import r2_score

def better_than_baseline(df, y):
    r2_model = r2_score(y, df.yhat)
    r2_baseline = r2_score(y, df.baseline)
    if r2_model > r2_baseline:
        print('Model perfomes better than baseline')
    else:
        print("Baseline performs better than model")


# # test

# In[17]:


df, train, validate, test = wrangle1.wrangle_zillow()


# In[18]:


x_train = train.drop(columns = 'taxvaluedollarcnt')
y_train = train.taxvaluedollarcnt
x_validate = validate.drop(columns = 'taxvaluedollarcnt')
y_validate = validate.taxvaluedollarcnt
x_test = test.drop(columns = 'taxvaluedollarcnt')
y_test = test.taxvaluedollarcnt


# In[19]:


r2_setup(train, x_train, y_train);


# In[20]:


regression_errors_mine(train);


# In[21]:


better_than_baseline(train, y_train)


# In[22]:


plot_residuals(y_train, train.yhat)


# In[ ]:





# # class

# In[9]:



#Dependencies for these functions
import math
from sklearn.metrics import mean_squared_error

def plot_residuals_c(y, yhat):
    residuals = yhat - y
    plt.scatter(x=y, y=residuals)
    plt.title('Residual plot')    

def regression_errors_c(y, yhat):
    sse = mean_squared_error(y, yhat) * len(y)
    ess = sum((yhat - y.mean()) ** 2)
    tss = sse + ess
    mse = mean_squared_error(y, yhat)
    rmse = sqrt(mse)
    return sse, ess, tss, mse, rmse

def baseline_mean_errors_c(y):
    sse = mean_squared_error(y, y.mean()) * len(y)
    mse = mean_squared_error(y, y.mean())
    rmse = sqrt(mse)
    return sse, mse, rmse

def better_than_baseline_c(y, yhat):
    sse = regression_errors(y, yhat)
    sse_b = baseline_mean_errors(y)
    if sse < sse_b:
        return True
    else:
        return False


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




