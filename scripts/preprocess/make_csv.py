
# coding: utf-8

# # Preporcesssing raw data and making CSV files

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data=[line.rstrip() for line in open('Bob.txt') ]


# In[3]:


col=['house_id','buid_date','date_priced','garden','dst_dock','dst_capital','dst_mkt','dst_tower','dst_river','renovation','dining_rooms','bedrooms','bathrooms','king_visit','curse','king_blessing','farm_land','locations','holy_tree','dst_knight']


# In[5]:


df=pd.DataFrame(columns=col)

#df


# In[6]:


df


# In[7]:


def to_df(arr,df,k):
    col=['house_id','buid_date','date_priced','garden','dst_dock','dst_capital','dst_mkt','dst_tower','dst_river','renovation','dining_rooms','bedrooms','bathrooms','king_visit','curse','king_blessing','farm_land','locations','holy_tree','dst_knight']
    tmp=pd.DataFrame(columns=col)
    
    for i in range(0,len(arr)):
        if 'House ID' in arr[i]:
            tmp.loc[k,'house_id']=arr[i].split(':')[1]

        elif 'Date Built' in arr[i]:
            tmp.loc[k,'buid_date']=arr[i].split('and')[0].split(':')[1]+':'+ arr[1].split('and')[0].split(':')[2]
            tmp.loc[k,'date_priced']=arr[i].split('and')[1].split(':')[1]+':'+ arr[1].split('and')[1].split(':')[2]

        elif 'beautiful garden' in arr[i]:
            tmp.loc[k,'garden']=1

        elif 'no space' in arr[i]:
            tmp.loc[k,'garden']=0

        elif 'the Dock' in arr[i]:
            tmp.loc[k,'dst_dock']=arr[i].split()[arr[i].split().index('holy')-1]

        elif 'Capital' in arr[i]:
            tmp.loc[k,'dst_capital']=arr[i].split()[arr[i].split().index('holy')-1]

        elif 'Royal Market' in arr[i]:
            tmp.loc[k,'dst_mkt']=arr[i].split()[arr[i].split().index('holy')-1]

        elif 'Guarding Tower' in arr[i]:
            tmp.loc[k,'dst_tower']=arr[i].split()[arr[i].split().index('holy')-1]

        elif 'the River' in arr[i]:
            tmp.loc[k,'dst_river']=arr[i].split()[arr[i].split().index('holy')-1]


        elif 'not undergo' in arr[i]:
            tmp.loc[k,'renovation']=0
        elif 'underwent renovation' in arr[i]:
            tmp.loc[k,'renovation']=1

        elif 'dining rooms' in arr[i]:
            tmp.loc[k,'dining_rooms']=arr[i].split()[arr[i].split().index('are')+1]

        elif 'bedrooms' in arr[i]:
            tmp.loc[k,'bedrooms']=arr[i].split()[arr[i].split().index('are')+1]

        elif 'bathrooms' in arr[i]:
            tmp.loc[k,'bathrooms']=arr[i].split()[arr[i].split().index('are')+1]


        elif 'curse this house' in arr[i]: 
            tmp.loc[k,'curse']=0
        elif 'cursed' in arr[i]: 
            tmp.loc[k,'curse']=1

        elif 'pay his visit' in arr[i]: 
            tmp.loc[k,'king_visit']=0   
        elif 'visited' in arr[i]: 
            tmp.loc[k,'king_visit']=1

        elif 'blessed the house' in arr[i]:
            tmp.loc[k,'king_blessing']=arr[i].split()[arr[i].split().index('with')+1]

        elif 'land of farm' in arr[i]: 
            tmp.loc[k,'farm_land']=arr[i].split()[arr[i].split().index('land')-1]

        elif 'Location of the house' in arr[i]: 
            tmp.loc[k,'locations']=arr[i].split(':')[1]

        elif 'stands tall' in arr[i]: 
            tmp.loc[k,'holy_tree']='yes'
        elif 'tree was cut' in arr[i]: 
            tmp.loc[k,'holy_tree']='no'

        elif 'Knight\'s house' in arr[i]:
            tmp.loc[k,'dst_knight']=arr[i].split()[arr[i].split().index('holy')-1]

    #print(tmp)
    df=df.append(tmp)
    return df
pass                 


# In[9]:


len(data)


# In[17]:


def make_csv(file_name):
    data=[line.rstrip() for line in open(file_name)]
    col=['house_id','buid_date','date_priced','garden','dst_dock','dst_capital','dst_mkt','dst_tower','dst_river','renovation','dining_rooms','bedrooms','bathrooms','king_visit','curse','king_blessing','farm_land','locations','holy_tree','dst_knight']
    df=pd.DataFrame(columns=col)
    
    i=0
    k=0
    while i <len(data):
        if 'House ID' in data[i]:
            l=i
            while data[i]!='':
                i=i+1
            r=i
            #print(k,data[l])
            df=to_df(data[l:r],df,k)
            k=k+1
        i=i+1
        
    file_csv=file_name.split('.')[0]+'.csv'
    df.to_csv(file_csv,index=None)
    print("CSV File Created!!! :))")
    return


# In[ ]:





# In[14]:


make_csv('Bob.txt')


# In[18]:


make_csv('Bright_Brothers.txt')


# In[21]:


make_csv('Masters_of_Stones.txt')


# In[22]:


make_csv('Not_Known.txt')


# In[23]:


make_csv('The_Greens.txt')


# In[24]:


make_csv('The_Kings.txt')


# In[25]:


make_csv('The_Lannisters.txt')


# In[26]:


make_csv('The_Ollivers.txt')


# In[27]:


make_csv('The_Overlords.txt')


# In[28]:


make_csv('The_Starks.txt')


# In[29]:


make_csv('Wood_Priests.txt')


# In[10]:


df.to_csv('Bob.csv',index=None)


# In[ ]:





# In[12]:


df

