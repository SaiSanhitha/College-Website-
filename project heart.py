#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split



heart= pd.read_csv('heart.csv')


# In[33]:


heart.columns = ['Age', 'Gender', 'ChestPain', 'RestingBloodPressure', 'Cholestrol', 'FastingBloodSugar', 'RestingECG', 'MaxHeartRateAchivied',
       'ExerciseIndusedAngina', 'Oldpeak', 'Slope', 'MajorVessels', 'Thalassemia', 'Target']


# In[40]:


heart



# In[35]:


import seaborn as sns


# In[36]:


result=[]
for i in heart['ChestPain']:
    if i == 0:
        result.append('Typical Angina')
    if i ==1:
        result.append('Atypical Angina')
    if i ==2:
        result.append('Non-Anginal')
    if i==3:
        result.append('Asymptomatic')
        
heart['ChestPainType']=pd.Series(result)


# In[37]:


import matplotlib.pyplot as plt
ax = sns.countplot(hue=result,x='Gender',data=heart,palette='husl')

plt.title("Chest Pain Type Vs Gender")    
plt.ylabel("")
plt.yticks([])
plt.xlabel("")
for p in ax.patches:
    ax.annotate(p.get_height(),(p.get_x()+0.05, p.get_height()+1))
ax.set_xticklabels(['Female','Male'])
print(ax.patches)


# In[38]:


import seaborn as sns
sns.countplot(x='Age',data=heart)
plt.show()


# In[39]:


ax = sns.regplot(x='Age', y='MaxHeartRateAchivied',data=heart, color="g")


