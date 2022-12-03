#!/usr/bin/env python
# coding: utf-8

# **Heart attack Data analysis**

# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# **2. Display Top 5 rows on the dataset**

# In[18]:


data=pd.read_csv('heart.csv')


# In[19]:


data.head()


# In[20]:


#1. Age
#2. Sex
#3. Chest pain type(4 values)
#     -Value 0: Typical angina
#     -Value 1: Atypical angina
#     -Value 2: non-anginal pain
#     -Value 3: Asyptomatic
#4. trestbps: resting blood pressure (in mm Hg on admission to the hospital)
#5. chol: serum cholestoral in mg/dl
#6. fbs: (fasting blood sugar > 120 g/dl) (1 =true; 0=false)
#7. restecg: resting electrocardiographic results
#     -Value 0: normal
#     -Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of> 0.05 mV)
#     -Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
# 8. thalach: maximum heart rate achieved
# 9. exang: exercise induced angina (1=yes, 0=no)
# 10. oldpeak =ST depression induced by exercise relative to rest
# 11. slope: the slope of the peak exercise ST segment\
#     -Value 1: upsloping 
#     -Value 2: flat
#     -Value 3: downsloping
# 12. ca: number of major vessels (0-3) coloured by flourosopy
# 13.thal: 3=normal; 6=fixed defect; 7=reversable defect
# 14. target: 0=less chance of heart attack, 1=more chance of heart attack
#  


# **3. Check last 5 rows of dataset**

# In[21]:


data.tail()


# **4. Shape of dataset(Number of rows and no. of columns)**

# In[22]:


data.shape


# In[23]:


print("Number of Rows", data.shape[0])
print("Number of columns",data.shape[1])


# **5. Get info about our dataset like total number of rows, Total number of rows, Total number of columns, Datatypes of Each column and memory requirements**

# In[25]:


data.info()


# **6. Check null values in the dataset**

# In[26]:


data.isnull().sum()


# **7. Check for duplicate data and drop them**

# In[35]:


data_dup=data.duplicated().any()
print(data_dup)


# In[36]:


data=data.drop_duplicates()


# In[37]:


data.shape


# **8. Get overall statistics about the dataset**

# In[38]:


data.describe()


# **9. Draw correlation matrix**

# In[41]:


plt.figure(figsize=(17,6))
sns.heatmap(data.corr(), annot=True)


# **10. How many people have heart disease, and how many don't have heart disease in this dataset?**

# In[42]:


data.columns 


# In[43]:


data['target'].value_counts()


# In[44]:


sns.countplot(data['target'])


# **11. Find count of male and female in the dataset**

# In[45]:


data.columns


# In[46]:


data['sex'].value_counts()


# In[51]:


sns.countplot(data['sex'])
plt.xticks([0,1],['Female','male'])
plt.show()


# **12. Find Gender distribution according to the target variable**

# In[52]:


data.columns 


# In[53]:


sns.countplot(x='sex', hue='target',data=data)
plt.xticks([1,0],['Male','Female'])
plt.legend(labels=['No-Disease','Disease'])
plt.show()


# **13. Check Age distribution in the dataset**

# In[55]:


sns.distplot(data['age'],bins=20)
plt.show()


# **14. Chest pain type**

# In[56]:


# Chest pain type(4 values)
#  -Value 0: typical angina
#  -Value 1: atypical angina
#  -Value 2: non-anginal pain
#  -Value 3: asymptomatic


# In[59]:


sns.countplot(data['cp'])
plt.xticks([0,1,2,3],["typical angina","atypical angina","non-anginal pain","asymptomatic"])
plt.xticks(rotation=75)
plt.show()


# **15. Shoe the chest pain distribution as per target variable**

# In[60]:


data.columns


# In[63]:


sns.countplot(x='cp',hue='target',data=data)
plt.legend(labels=["No-disease","disease"])
plt.show()


# **16. Show fasting blood sugar distribution according to target variable**

# In[65]:


sns.countplot(x='fbs',hue='target',data=data)
plt.legend(labels=["No-disease","disease"])
plt.show()


# **17. Check Resting blood pressure distribution**

# In[66]:


data.columns


# In[67]:


data['trestbps'].hist()


# **18. Compare resting blood pressure as per sex column**

# In[71]:


g=sns.FacetGrid(data,hue="sex",aspect=4)
g.map(sns.kdeplot,'trestbps', shade=True)
plt.legend(labels=['Male','Female'])


# **19. Show distribution of serum cholestrol**

# In[72]:


data.columns


# In[73]:


data['chol'].hist()


# **20. Plot Continuous variables**

# In[74]:


data.columns


# In[76]:


cate_val=[]
cont_val=[]

for column in data.columns:
    if data[column].nunique() <=10:
        cate_val.append(column)
    else:
        cont_val.append(column)


# In[77]:


cate_val


# In[78]:


cont_val


# In[82]:


data.hist(cont_val,figsize=(15,6))
plt.tight_layout()
plt.show()


# In[ ]:




