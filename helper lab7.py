# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:57:14 2018

@author: marek
"""

import os
os.chdir('D://Quant/ox-p4ds-master/notebooks/')

import pandas as pd

df = pd.read_csv('nasa_access_log_aug95_short.csv')
df.columns = ['Address', 'DateTime','Timezone',',Method','File','HTTP','Status','Size']

with open('nasa_access_log_aug95_short.txt') as input_file_pointer:
    for line in input_file_pointer:
        data=line.replace(' - - ', ',').replace('"','').replace('[',' ').replace(']','').split()
        if len(data)==8:
            list_df.append({'Address':data[0],
                       'DateTime':data[1],
                       'Timezone':data[2],
                       'Method':data[3],
                       'File':data[4],
                       'HTTP':data[5],
                       'Status':data[6],
                       'Size':data[7]},
                     ignore_index=True)


SUE_MC=pd.DataFrame((SUE_portfolio1*MCapRank).mean(1).resample('A').mean(),columns=['SUE1'])
SUE_MC['SUE2']=(SUE_portfolio2*MCapRank).mean(1).resample('A').mean()
SUE_MC['SUE3']=(SUE_portfolio3*MCapRank).mean(1).resample('A').mean()
SUE_MC['SUE4']=(SUE_portfolio4*MCapRank).mean(1).resample('A').mean()
SUE_MC['SUE5']=(SUE_portfolio5*MCapRank).mean(1).resample('A').mean()
SUE_MC['SUE6']=(SUE_portfolio6*MCapRank).mean(1).resample('A').mean()
SUE_MC['SUE7']=(SUE_portfolio7*MCapRank).mean(1).resample('A').mean()
SUE_MC['SUE8']=(SUE_portfolio8*MCapRank).mean(1).resample('A').mean()
SUE_MC['SUE9']=(SUE_portfolio9*MCapRank).mean(1).resample('A').mean()
SUE_MC['SUE10']=(SUE_portfolio10*MCapRank).mean(1).resample('A').mean()

SUE_MC.to_csv('D://Doktorat Marek//dane//Results//Analysts//SUE_MCapRank.csv',encoding='UTF-8')

SUE_Beta=pd.DataFrame((SUE_portfolio1*Beta).mean(1).resample('A').mean(),columns=['SUE1'])
SUE_Beta['SUE2']=(SUE_portfolio2*Beta).mean(1).resample('A').mean()
SUE_Beta['SUE3']=(SUE_portfolio3*Beta).mean(1).resample('A').mean()
SUE_Beta['SUE4']=(SUE_portfolio4*Beta).mean(1).resample('A').mean()

SUE_Beta.to_csv('D://Doktorat Marek//dane//Results//Analysts//SUE_Beta.csv',encoding='UTF-8')
