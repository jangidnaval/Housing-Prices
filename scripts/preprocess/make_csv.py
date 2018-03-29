
# coding: utf-8

# # Preporcesssing raw data and making CSV files

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


data=[line.rstrip() for line in open('Bob.txt') ]


# In[5]:


col=['house_id','buid_date','date_priced','garden','dst_dock','dst_capital','dst_mkt','dst_tower','dst_river','renovation','dining_rooms','bedrooms','bathrooms','king_visit','curse','king_blessing','farm_land','locations','holy_tree','dst_knight','builder']


# In[15]:


df=pd.DataFrame(columns=col)

#df


# In[7]:


df


# In[219]:


#be carefull
#remove unnessesary/extra spaces from values (nhi to baad me join na ho payega price se .....)
# use str=str.strip()



def to_df(arr,df,k,builder):
    col=['house_id','buid_date','date_priced','garden','dst_dock','dst_capital','dst_mkt','dst_tower','dst_river','renovation','dining_rooms','bedrooms','bathrooms','king_visit','curse','king_blessing','farm_land','locations','holy_tree','dst_knight','builder']
    tmp=pd.DataFrame(columns=col)
    
    for i in range(0,len(arr)):
        tmp.loc[k,'builder']=builder
        if 'House ID' in arr[i]:
            tmp.loc[k,'house_id']=arr[i].split(':')[1].strip()

        elif 'Date Built' in arr[i]:
            tmp.loc[k,'buid_date']=arr[i].split('and')[0].split(':')[1]+':'+ arr[1].split('and')[0].split(':')[2].strip()
            tmp.loc[k,'date_priced']=arr[i].split('and')[1].split(':')[1]+':'+ arr[1].split('and')[1].split(':')[2].strip()

        elif 'beautiful garden' in arr[i]:
            tmp.loc[k,'garden']=1

        elif 'no space' in arr[i]:
            tmp.loc[k,'garden']=0

        elif 'the Dock' in arr[i]:
            tmp.loc[k,'dst_dock']=arr[i].split()[arr[i].split().index('holy')-1].strip()

        elif 'Capital' in arr[i]:
            tmp.loc[k,'dst_capital']=arr[i].split()[arr[i].split().index('holy')-1].strip()

        elif 'Royal Market' in arr[i]:
            tmp.loc[k,'dst_mkt']=arr[i].split()[arr[i].split().index('holy')-1].strip()

        elif 'Guarding Tower' in arr[i]:
            tmp.loc[k,'dst_tower']=arr[i].split()[arr[i].split().index('holy')-1].strip()

        elif 'the River' in arr[i]:
            tmp.loc[k,'dst_river']=arr[i].split()[arr[i].split().index('holy')-1].strip()


        elif 'not undergo' in arr[i]:
            tmp.loc[k,'renovation']=0
        elif 'underwent renovation' in arr[i]:
            tmp.loc[k,'renovation']=1

        elif 'dining rooms' in arr[i]:
            tmp.loc[k,'dining_rooms']=arr[i].split()[arr[i].split().index('are')+1].strip()

        elif 'bedrooms' in arr[i]:
            tmp.loc[k,'bedrooms']=arr[i].split()[arr[i].split().index('are')+1].strip()

        elif 'bathrooms' in arr[i]:
            tmp.loc[k,'bathrooms']=arr[i].split()[arr[i].split().index('are')+1].strip()


        elif 'curse this house' in arr[i]: 
            tmp.loc[k,'curse']=0
        elif 'cursed' in arr[i]: 
            tmp.loc[k,'curse']=1

        elif 'pay his visit' in arr[i]: 
            tmp.loc[k,'king_visit']=0   
        elif 'visited' in arr[i]: 
            tmp.loc[k,'king_visit']=1

        elif 'blessed the house' in arr[i]:
            tmp.loc[k,'king_blessing']=arr[i].split()[arr[i].split().index('with')+1].strip()

        elif 'land of farm' in arr[i]: 
            tmp.loc[k,'farm_land']=arr[i].split()[arr[i].split().index('land')-1].strip()

        elif 'Location of the house' in arr[i]: 
            tmp.loc[k,'locations']=arr[i].split(':')[1].strip()

        elif 'stands tall' in arr[i]: 
            tmp.loc[k,'holy_tree']='yes'
        elif 'tree was cut' in arr[i]: 
            tmp.loc[k,'holy_tree']='no'

        elif 'Knight\'s house' in arr[i]:
            tmp.loc[k,'dst_knight']=arr[i].split()[arr[i].split().index('holy')-1].strip()

    #print(tmp)
    df=df.append(tmp)
    return df
pass                 


# In[9]:


len(data)


# In[220]:


def merge_df(file_name,df):
    data=[line.rstrip() for line in open(file_name)]
    #col=['house_id','buid_date','date_priced','garden','dst_dock','dst_capital','dst_mkt','dst_tower','dst_river','renovation','dining_rooms','bedrooms','bathrooms','king_visit','curse','king_blessing','farm_land','locations','holy_tree','dst_knight','builder']
    #df=pd.DataFrame(columns=col)
    
    i=0
    k=df.index.size
    builder=file_name.split('.')[0]
    while i <len(data):
        if 'House ID' in data[i]:
            l=i
            while data[i]!='':
                i=i+1
            r=i
            #print(k,data[l])
            df=to_df(data[l:r],df,k,builder)
            k=k+1
        i=i+1
       
    
    #file_csv=file_name.split('.')[0]+'.csv'
    #df.to_csv(file_csv,index=None)
    print(file_name,' added to data frame')
    return df


# In[ ]:





# In[29]:


col=['house_id','buid_date','date_priced','garden','dst_dock','dst_capital','dst_mkt','dst_tower','dst_river','renovation','dining_rooms','bedrooms','bathrooms','king_visit','curse','king_blessing','farm_land','locations','holy_tree','dst_knight','builder']
df=pd.DataFrame(columns=col)


# In[30]:


df.index.size


# In[42]:


df=merge_df('Bob.txt',df)


# In[ ]:


df.index.size


# In[ ]:


df=merge_df('Bright_Brothers.txt',df)


# In[ ]:


df.tail()


# In[39]:


files=['Bob.txt','Bright_Brothers.txt','Masters_of_Stones.txt','The_Overlords.txt','Wood_Priests.txt','The_Starks.txt','The_Greens.txt','The_Kings.txt','The_Lannisters.txt','The_Ollivers.txt','Not_Known.txt']


# In[41]:


len(files)


# In[222]:


def final_csv(df):
    files=['Bob.txt','Bright_Brothers.txt','Masters_of_Stones.txt','The_Overlords.txt','Wood_Priests.txt','The_Starks.txt','The_Greens.txt','The_Kings.txt','The_Lannisters.txt','The_Ollivers.txt','Not_Known.txt']
    for i in range (0,len(files)):
        df=merge_df(files[i],df)
    
    #csv file with detail of all the builders and houses 
    df.to_csv('final_csv.csv',index=None)
    print('final data frame created')
    return df
    


# In[223]:


col=['house_id','buid_date','date_priced','garden','dst_dock','dst_capital','dst_mkt','dst_tower','dst_river','renovation','dining_rooms','bedrooms','bathrooms','king_visit','curse','king_blessing','farm_land','locations','holy_tree','dst_knight','builder']
df=pd.DataFrame(columns=col)
df=final_csv(df)


# In[ ]:


#merging data frame based on some columns
#new_df=pd.merge(df1,df2,how='inner',on=['col1','col2'])


# In[237]:


df=pd.read_csv('final_csv.csv')
#adding prices with created csv and dataframe
price=pd.read_csv('house_prices.csv')
missing=pd.read_csv('missing.csv')
#rename column names
price.columns=['house_id','price']
missing.columns=['house_id']
train_data=pd.merge(df,price,how='inner',on=['house_id'])
test_data=pd.merge(df,missing,how='inner',on=['house_id'])

train_data.to_csv('train.csv',index=None)
test_data.to_csv('test.csv',index=None)


# In[228]:


missing


# In[225]:


type(price['house_id'][0])


# In[226]:


train_data


# In[167]:


type(df)


# In[84]:


df.house_id=df.house_id.astype(str)


# In[92]:


df.dtypes


# In[93]:


price.dtypes


# In[94]:


type(df['house_id'])


# In[135]:


train_data=pd.merge(df,price,how='inner',on=['house_id'])


# In[136]:


train_data


# In[74]:


train_data


# In[67]:


train_data


# In[14]:


dfmake_csv('Bob.txt')

make_csv('Bright_Brothers.txt')

make_csv('Masters_of_Stones.txt')

make_csv('Not_Known.txt')

make_csv('The_Greens.txt')

make_csv('The_Kings.txt')

make_csv('The_Lannisters.txt')

make_csv('The_Ollivers.txt')

make_csv('The_Overlords.txt')

make_csv('The_Starks.txt')

make_csv('Wood_Priests.txt')



# In[12]:


df


# In[8]:


df


# In[17]:





# In[11]:


df


# In[142]:


d1=price


# In[238]:


#d1


# In[140]:


d=df


# In[141]:


d


# In[144]:


d=d.set_index('house_id')


# In[145]:


d1=price


# In[146]:


d1=d1.set_index('house_id')


# In[147]:


d3=pd.concat([d1,d],axis=1,join='inner')


# In[148]:


d3


# In[149]:


type(price['house_id'])


# In[150]:


price=price.dropna()


# In[152]:


d1.index


# In[157]:


type(d1.index)


# In[164]:


train


# In[211]:


len(df.loc[0,'house_id'])


# In[212]:


len(price.loc[0,'house_id'])

