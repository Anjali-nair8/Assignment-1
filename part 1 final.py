#!/usr/bin/env python
# coding: utf-8

# # Wallmart

# In[1]:


# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# Read CSV
df = pd.read_csv("../Input/WalmartFinal.csv")


# In[3]:


# View Data
df.head()


# In[4]:


# View Total Sum
df.mean()


# In[5]:


# 1. Find the average of total sales for days that are holidays and days that are non-holidays. Comment on the differences observed
YesHoliday = df.loc[df['Holiday_Flag'] == 1, 'Weekly_Sales'].mean()
YesHoliday


# In[6]:


NoHoliday = df.loc[df['Holiday_Flag'] == 0, 'Weekly_Sales'].mean()
NoHoliday


# ### Differences Observed
# Looking at the fact that total sales averages during holidays are higher than non holidays, it would seem that people prefer to shop during holidays.

# In[7]:


# 2. Provide descriptive statistics of all features in the dataset
df.describe()


# ## 3. Complete a correlation matrix and explain the relationship of each feature compared to Sales and whether they are correlated to each other.

# In[8]:


df.corr()


# ### Sales to Store
# It is non applicable because although it would indicate that higher store # would mean more sales, this would make no practical sense, since the store # is just a unique id.
# 
# ### Sales to Sales 
# It is a perfect correlation because it is the same variable.
# 
# ### Sales to holiday
# From the first question and the correlation matrix we know that holidays seems to have a higher sales amount over non holidays.
# 
# ### Sales to Temperature
# It would seem that a higher temperature results in a bery slight almost insignificant reduction in sales.
# 
# ### Sales to Fuel Price
# While it is a positive correlation it is such a low value that it is statistically insignificant and we could conclude thereis no correlation.
# 
# ### Sales to CPI
# The higher the CPI the lower the sales, but at a really low correlation value.
# 
# ### Sales to unemployment
# If unemployment increases it would seem that sales decrease slightly.

# ## 4. Create a scatter plot comparing sales to each feature to visualize the influence it has on sales. Please elaborate on what you observe

# In[9]:


xs = np.array((df.Weekly_Sales,df.Weekly_Sales,df.Weekly_Sales,df.Weekly_Sales,df.Weekly_Sales,df.Weekly_Sales))
ys = np.array((df.Store, df.Holiday_Flag, df.Temperature, df.Fuel_Price, df.CPI, df.Unemployment))

for x, y in zip(xs, ys):
    plt.scatter(x, y, cmap="copper", alpha = 0.3)
plt.show()


# ## 5.	Plot Weekly sales vs date and comment on trends or seasonality that can be observed. (*Hint to do this you will need to aggregate by date and sum the weekly sales numbers)

# In[20]:


df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%y")
dfPlot = df.sort_values(by=['Date']).groupby('Date').agg({'Weekly_Sales':['sum']})
dfPlot


# In[21]:


dfPlot = dfPlot.reset_index()


# In[22]:


dfPlot


# In[26]:


dfPlot.plot(x='Date', y='Weekly_Sales',kind="line")
plt.show()

