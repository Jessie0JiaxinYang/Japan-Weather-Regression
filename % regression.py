# 

import pandas as pd 
import numpy as np
from pandas import DataFrame
import datetime

import pandas
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\RBAC 2021\\Weather Seasonality\\Results\\Based on %\\Japan Output\\Kochi Output3.xlsx'
sheetName = 'Sheet1'
table = pd.read_excel(file_path,sheet_name=sheetName)
table = table.iloc[6:,0:]
table.columns = ['ID', 'sector', 'year', 'month', 'area', 'value', 'date', 'days', 'valuedaily', \
'CDD', 'HDD', 'com', 'res', 'ind', 'comHDD', 'resHDD', 'indHDD', 'comCDD', 'resCDD', 'indCDD', 'CMA', 'Hist Dev%']
table[['CDD']] = table[['CDD']].astype('float')
table[['HDD']] = table[['HDD']].astype('float')
table[['com']] = table[['com']].astype('float')
table[['res']] = table[['res']].astype('float')
table[['ind']] = table[['ind']].astype('float')
table[['comHDD']] = table[['comHDD']].astype('float')
table[['resHDD']] = table[['resHDD']].astype('float')
table[['indHDD']] = table[['indHDD']].astype('float')
table[['comCDD']] = table[['comCDD']].astype('float')
table[['resCDD']] = table[['resCDD']].astype('float')
table[['indCDD']] = table[['indCDD']].astype('float')
table[['Hist Dev%']] = table[['Hist Dev%']].astype('float')

x = sm.add_constant(table.iloc[:,9:20]) #生成自变量
y = table['Hist Dev%']
model = sm.OLS(y, x)
result = model.fit()
result.summary()
 