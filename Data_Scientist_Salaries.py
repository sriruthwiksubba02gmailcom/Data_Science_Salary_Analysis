#!/usr/bin/env python
# coding: utf-8

# ## Problem Statement

# We are given the hestoric data of different data science fields and we are asked to analyse and draw atleat 3 inferences from it.

# In[7]:


#IMPORTING NEEDED LIBRARIES


# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import csv 
import warnings
warnings.filterwarnings('ignore')
sns.set(style='whitegrid',palette='hsv')

df=pd.read_csv("C:\\Users\\subba\\OneDrive\\Desktop\\Data Science Salaries\\ds_salaries.csv")


# In[3]:


df.head(7)


# In[6]:


df.describe()


# In[3]:


df['work_year'].value_counts()


# In[4]:


df['experience_level'].value_counts()


# In[5]:


df['company_size'].value_counts()


# ### It is given that the data collected has no missing values.

# In[7]:


df.isnull().sum()


# # Drawing insights

# ## 1.Salaries based on jobs

# In[9]:


df['salary_in_usd'].groupby(df['job_title']).mean()


# In[29]:


jobs= df[df['work_year']==2023]['job_title'].value_counts().nlargest(10)


# In[30]:


jobs


# Data Engineers,Data Scientists and Data Analysts are at the top 3 positions 

# ## 2.Salaries based on work experience 

# In[20]:


df['salary_in_usd'].groupby(df['experience_level']).mean()


# In[36]:


# This is the right scenario where we have to use the "boxplot" to analyse the avg salaries to corr experience level 

SE= Senior Level
MI= Mid-Level
SE= Senior Level
EX= Executive Level
# In[34]:


sns.boxplot(x='experience_level', y='salary_in_usd', data=df)


# Here we can witness that, 
# EX are having largest salries between 300000 to 400000.
# SE wiht avg salary is about 300000 but also increase and reachs 400000
# then followed by MI and EN
# 

# ## 3.Salaries based on work year 

# In[37]:


comapany_salary=np.array(df['salary_in_usd'].groupby(df['work_year']) .mean())
sns.barplot(x='work_year', y='salary_in_usd', data=df)

Here we can see that demand for this jobs are relatively high with increasong salary