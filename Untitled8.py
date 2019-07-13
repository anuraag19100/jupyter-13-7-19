#!/usr/bin/env python
# coding: utf-8

# ### Transforming Code intlo Idiomatic Python
# - Replace traditional index manupulation with Python core looping idiomatic

# In[2]:


# Looping over a range of numbers - Traditional Approach
for i in [0,1,2,3,4,5]:
   print(i**2,end=" ")


# In[1]:


# Idiomatic Programming
for i in range(6):
    print(i**2,end=" ")


# ### Looping Over a Collection

# In[3]:


colors = ['red','green','yellow','purple']
for i in range(len(colors)):
    print(colors[i],end=" ")


# In[4]:


for color in colors:
    print(color,end=" ")


# ### Looping backwards

# In[5]:


colors = ['red','green','yellow','purple']
for i in range(len(colors)-1,-1,-1):
    print(colors[i],end=" ")


# In[6]:


for color in reversed(colors):
    print(color,end=" ")
    


# In[9]:


colors = ['red','green','yellow','purple']
for color in sorted(colors,reverse=True):
    print(color,end=" ")


# In[10]:


colors = ['red','green','yellow','purple']
for color in sorted(colors):
    print(color,end=" ")


# ###
# - if x <=y and y <=z:
# - if x<=y<=z:
# - if x==True:
# - if x:

# ### Pandas

# In[11]:


import pandas as pd


# In[17]:


dt = {'Id':[11,12,13,14,15],
      'first_name':['A','B','C','D','E'],
      'Company':['aa','bb','cc','dd','ee'],
      'address':['Hyd','Hyd','Hyd','Hyd','Hyd']}
mydt = pd.DataFrame(dt)


# In[18]:


print(mydt)


# In[28]:


import os


# In[30]:


os.chdir("pathfile")


# In[29]:


os.mkdir("pathfile")


# In[26]:


mydt.to_csv('workingFile.csv',index = False)


# In[41]:


pwd


# ### Reading the data from CSV file

# In[39]:


mydata = pd.read_csv('workingFile.csv')


# In[40]:


pwd


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




