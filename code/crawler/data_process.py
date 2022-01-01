import pandas as pd
import numpy as np

#处理104holland
df = pd.read_csv('./104hollland.csv',index_col =0)
df.duplicated(subset=['jobCat'])

t = df.drop_duplicates(subset=['jobCat'])

b = df.drop_duplicates(subset=['jobName'])

df = t

df.to_csv('./104Jobs.csv',index = 0,encoding = 'utf_8_sig')

#处理related相关
df_related = pd.read_csv('./relatedjob.csv',index_col= 0 )
df_related.drop('jobCat',inplace = True,axis =1 )
df_related = df_related[['JobCat','relatedJob']]
df_related.to_csv('./relatedjob.csv',index = 0)