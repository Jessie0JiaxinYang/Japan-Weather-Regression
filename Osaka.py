

# Japan By region, non-elc, regression
# ** Osaka

## 2018 
import pandas as pd 
import numpy as np
from pandas import DataFrame
import datetime


starttime = datetime.datetime.now()

#文件路径
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\2018 Summary Japan.xlsx'
# Jan
# 读取sheet的名字
sheetName = '地区別表（数量）201801'
table = pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "1", "Osaka", table.iloc[19,10]],\
["com", "2018", "1", "Osaka", table.iloc[20,10]],\
["ind", "2018", "1", "Osaka", table.iloc[21,10]],\
["oth", "2018", "1", "Osaka", table.iloc[22,10]]]
d201801 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Feb 
sheetName='地区別表（数量）201802'
table = pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "2", "Osaka", table.iloc[19,10]],\
["com", "2018", "2", "Osaka", table.iloc[20,10]],\
["ind", "2018", "2", "Osaka", table.iloc[21,10]],\
["oth", "2018", "2", "Osaka", table.iloc[22,10]]]
d201802 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Mar 
sheetName = '地区別表（数量）201803'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "3", "Osaka", table.iloc[19,10]],\
["com", "2018", "3", "Osaka", table.iloc[20,10]],\
["ind", "2018", "3", "Osaka", table.iloc[21,10]],\
["oth", "2018", "3", "Osaka", table.iloc[22,10]]]
d201803 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Apr 
sheetName = '地区別表（数量）201804'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "4", "Osaka", table.iloc[19,10]],\
["com", "2018", "4", "Osaka", table.iloc[20,10]],\
["ind", "2018", "4", "Osaka", table.iloc[21,10]],\
["oth", "2018", "4", "Osaka", table.iloc[22,10]]]
d201804 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# May 
sheetName = '地区別表（数量）201805'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "5", "Osaka", table.iloc[19,10]],\
["com", "2018", "5", "Osaka", table.iloc[20,10]],\
["ind", "2018", "5", "Osaka", table.iloc[21,10]],\
["oth", "2018", "5", "Osaka", table.iloc[22,10]]]
d201805 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Jun 
sheetName = '地区別表（数量）201806'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "6", "Osaka", table.iloc[19,10]],\
["com", "2018", "6", "Osaka", table.iloc[20,10]],\
["ind", "2018", "6", "Osaka", table.iloc[21,10]],\
["oth", "2018", "6", "Osaka", table.iloc[22,10]]]
d201806 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Jul 
sheetName = '地区別表（数量）201807'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "7", "Osaka", table.iloc[19,10]],\
["com", "2018", "7", "Osaka", table.iloc[20,10]],\
["ind", "2018", "7", "Osaka", table.iloc[21,10]],\
["oth", "2018", "7", "Osaka", table.iloc[22,10]]]
d201807 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Aug 
sheetName = '地区別表（数量）201808 '
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "8", "Osaka", table.iloc[19,10]],\
["com", "2018", "8", "Osaka", table.iloc[20,10]],\
["ind", "2018", "8", "Osaka", table.iloc[21,10]],\
["oth", "2018", "8", "Osaka", table.iloc[22,10]]]
d201808 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Sep 
sheetName = '地区別表（数量）201809'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "9", "Osaka", table.iloc[19,10]],\
["com", "2018", "9", "Osaka", table.iloc[20,10]],\
["ind", "2018", "9", "Osaka", table.iloc[21,10]],\
["oth", "2018", "9", "Osaka", table.iloc[22,10]]]
d201809 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Oct 
sheetName = '地区別表（数量）201810'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "10", "Osaka", table.iloc[19,10]],\
["com", "2018", "10", "Osaka", table.iloc[20,10]],\
["ind", "2018", "10", "Osaka", table.iloc[21,10]],\
["oth", "2018", "10", "Osaka", table.iloc[22,10]]]
d201810 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Nov 
sheetName = '地区別表（数量）201811'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "11", "Osaka", table.iloc[19,10]],\
["com", "2018", "11", "Osaka", table.iloc[20,10]],\
["ind", "2018", "11", "Osaka", table.iloc[21,10]],\
["oth", "2018", "11", "Osaka", table.iloc[22,10]]]
d201811 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Dec 
sheetName = '地区別表（数量）201812'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "12", "Osaka", table.iloc[19,10]],\
["com", "2018", "12", "Osaka", table.iloc[20,10]],\
["ind", "2018", "12", "Osaka", table.iloc[21,10]],\
["oth", "2018", "12", "Osaka", table.iloc[22,10]]]
d201812 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])


## 2019 

#文件路径
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201901 Japan.xlsx'
# Jan
# 读取sheet的名字
sheetName = '地区別表（数量）201901'
table = pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "1", "Osaka", table.iloc[19,10]],\
["com", "2019", "1", "Osaka", table.iloc[20,10]],\
["ind", "2019", "1", "Osaka", table.iloc[21,10]],\
["oth", "2019", "1", "Osaka", table.iloc[22,10]]]
d201901 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Feb 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201902 Japan.xlsx'
sheetName='地区別表（数量）201902'
table = pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "2", "Osaka", table.iloc[19,10]],\
["com", "2019", "2", "Osaka", table.iloc[20,10]],\
["ind", "2019", "2", "Osaka", table.iloc[21,10]],\
["oth", "2019", "2", "Osaka", table.iloc[22,10]]]
d201902 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Mar 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201903 Japan.xlsx'

sheetName = '地区別表（数量）201903'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "3", "Osaka", table.iloc[19,10]],\
["com", "2019", "3", "Osaka", table.iloc[20,10]],\
["ind", "2019", "3", "Osaka", table.iloc[21,10]],\
["oth", "2019", "3", "Osaka", table.iloc[22,10]]]
d201903 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Apr 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201904 Japan.xlsx'
sheetName = '地区別表（数量）201904'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "4","Osaka", table.iloc[19,10]],\
["com", "2019", "4", "Osaka", table.iloc[20,10]],\
["ind", "2019", "4", "Osaka", table.iloc[21,10]],\
["oth", "2019", "4", "Osaka", table.iloc[22,10]]]
d201904 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# May 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201905 Japan.xlsx'
sheetName = '地区別表（数量）201905'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "5", "Osaka", table.iloc[19,10]],\
["com", "2019", "5", "Osaka", table.iloc[20,10]],\
["ind", "2019", "5", "Osaka", table.iloc[21,10]],\
["oth", "2019", "5", "Osaka", table.iloc[22,10]]]
d201905 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Jun
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201906 Japan.xlsx' 
sheetName = '地区別表（数量）201906'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "6", "Osaka", table.iloc[19,10]],\
["com", "2019", "6", "Osaka", table.iloc[20,10]],\
["ind", "2019", "6", "Osaka", table.iloc[21,10]],\
["oth", "2019", "6", "Osaka", table.iloc[22,10]]]
d201906 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Jul 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201907 Japan.xlsx'
sheetName = '地区別表（数量）201907'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "7", "Osaka", table.iloc[19,10]],\
["com", "2019", "7", "Osaka", table.iloc[20,10]],\
["ind", "2019", "7", "Osaka", table.iloc[21,10]],\
["oth", "2019", "7", "Osaka", table.iloc[22,10]]]
d201907 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Aug 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201908 Japan.xlsx'
sheetName = '地区別表（数量）201908'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "8", "Osaka", table.iloc[19,10]],\
["com", "2019", "8", "Osaka", table.iloc[20,10]],\
["ind", "2019", "8", "Osaka", table.iloc[21,10]],\
["oth", "2019", "8", "Osaka", table.iloc[22,10]]]
d201908 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Sep 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201909 Japan.xlsx'
sheetName = '地区別表（数量）201909'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "9", "Osaka", table.iloc[19,10]],\
["com", "2019", "9", "Osaka", table.iloc[20,10]],\
["ind", "2019", "9", "Osaka", table.iloc[21,10]],\
["oth", "2019", "9", "Osaka", table.iloc[22,10]]]
d201909 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Oct 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201910 Japan.xlsx'
sheetName = '地区別表（数量）201910'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "10", "Osaka", table.iloc[19,10]],\
["com", "2019", "10", "Osaka", table.iloc[20,10]],\
["ind", "2019", "10", "Osaka", table.iloc[21,10]],\
["oth", "2019", "10", "Osaka", table.iloc[22,10]]]
d201910 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Nov 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201911 Japan.xlsx'
sheetName = '地区別表（数量）201911'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "11", "Osaka", table.iloc[19,10]],\
["com", "2019", "11", "Osaka", table.iloc[20,10]],\
["ind", "2019", "11", "Osaka", table.iloc[21,10]],\
["oth", "2019", "11", "Osaka", table.iloc[22,10]]]
d201911 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Dec 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201912 Japan.xlsx'
sheetName = '地区別表（数量）201912'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "12", "Osaka", table.iloc[19,10]],\
["com", "2019", "12", "Osaka", table.iloc[20,10]],\
["ind", "2019", "12", "Osaka", table.iloc[21,10]],\
["oth", "2019", "12", "Osaka", table.iloc[22,10]]]
d201912 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

## 2020 


#文件路径
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202001 Japan.xlsx'
# Jan
# 读取sheet的名字
sheetName = '地区別表（数量）202001'
table = pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "1", "Osaka", table.iloc[19,10]],\
["com", "2020", "1", "Osaka", table.iloc[20,10]],\
["ind", "2020", "1", "Osaka", table.iloc[21,10]],\
["oth", "2020", "1", "Osaka", table.iloc[22,10]]]
d202001 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Feb 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202002 Japan.xlsx'
sheetName='地区別表（数量）202002'
table = pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "2", "Osaka", table.iloc[19,10]],\
["com", "2020", "2", "Osaka", table.iloc[20,10]],\
["ind", "2020", "2", "Osaka", table.iloc[21,10]],\
["oth", "2020", "2", "Osaka", table.iloc[22,10]]]
d202002 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Mar 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202003 Japan.xlsx'

sheetName = '地区別表（数量）202003'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "3", "Osaka", table.iloc[19,10]],\
["com", "2020", "3", "Osaka", table.iloc[20,10]],\
["ind", "2020", "3", "Osaka", table.iloc[21,10]],\
["oth", "2020", "3", "Osaka", table.iloc[22,10]]]
d202003 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Apr 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202004 Japan.xlsx'
sheetName = '地区別表（数量）202004'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "4", "Osaka", table.iloc[19,10]],\
["com", "2020", "4", "Osaka", table.iloc[20,10]],\
["ind", "2020", "4", "Osaka", table.iloc[21,10]],\
["oth", "2020", "4", "Osaka", table.iloc[22,10]]]
d202004 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# May 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202005 Japan.xlsx'
sheetName = '地区別表（数量）202005'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "5", "Osaka", table.iloc[19,10]],\
["com", "2020", "5", "Osaka", table.iloc[20,10]],\
["ind", "2020", "5", "Osaka", table.iloc[21,10]],\
["oth", "2020", "5", "Osaka", table.iloc[22,10]]]
d202005 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Jun
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202006 Japan.xlsx' 
sheetName = '地区別表（数量）202006'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "6", "Osaka", table.iloc[19,10]],\
["com", "2020", "6", "Osaka", table.iloc[20,10]],\
["ind", "2020", "6", "Osaka", table.iloc[21,10]],\
["oth", "2020", "6", "Osaka", table.iloc[22,10]]]
d202006 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Jul 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202007 Japan.xlsx'
sheetName = '地区別表（数量）202007'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "7", "Osaka", table.iloc[19,10]],\
["com", "2020", "7", "Osaka", table.iloc[20,10]],\
["ind", "2020", "7", "Osaka", table.iloc[21,10]],\
["oth", "2020", "7", "Osaka", table.iloc[22,10]]]
d202007 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

# Aug 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202008 Japan.xlsx'
sheetName = '地区別表（数量）202008'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "8", "Osaka", table.iloc[19,10]],\
["com", "2020", "8", "Osaka", table.iloc[20,10]],\
["ind", "2020", "8", "Osaka", table.iloc[21,10]],\
["oth", "2020", "8", "Osaka", table.iloc[22,10]]]
d202008 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])


# Sep 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202009 Japan.xlsx'
sheetName = '地区別表（数量）202009'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "9", "Osaka", table.iloc[19,10]],\
["com", "2020", "9", "Osaka", table.iloc[20,10]],\
["ind", "2020", "9", "Osaka", table.iloc[21,10]],\
["oth", "2020", "9", "Osaka", table.iloc[22,10]]]
d202009 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])
# Oct 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202010 Japan.xlsx'
sheetName = '地区別表（数量）202010'
table=pd.read_excel(file_path,sheet_name=sheetName)
data = [["res", "2020", "10", "Osaka", table.iloc[19,10]],\
["com", "2020", "10", "Osaka", table.iloc[20,10]],\
["ind", "2020", "10", "Osaka", table.iloc[21,10]],\
["oth", "2020", "10", "Osaka", table.iloc[22,10]]]
d202010 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])


# Nov 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202011 Japan.xlsx'
sheetName = '地区別表（数量）202011'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "11", "Osaka", table.iloc[18,12]],\
["com", "2020", "11", "Osaka", table.iloc[19,12]],\
["ind", "2020", "11", "Osaka", table.iloc[20,12]],\
["oth", "2020", "11", "Osaka", table.iloc[21,12]]]
d202011 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])

''' 
# Dec 
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202012 Japan.xlsx'
sheetName = '地区別表（数量）202012'
table=pd.read_excel(file_path,sheet_name=sheetName)
data = [["res", "2020", "12", table.iloc[19,6]],\
["com", "2020", "12", table.iloc[20,6]],\
["ind", "2020", "12", table.iloc[21,6]],\
["oth", "2020", "12", table.iloc[22,6]]]
d202012 = pd.DataFrame(data,columns= ["sector", "year", "month", "area", "value"])
'''

###############3

Output1 = [d201801, d201802, d201803, d201804, d201805, d201806, d201807, d201808, d201809, d201810, d201811, d201812, \
d201901, d201902, d201903, d201904, d201905, d201906, d201907, d201908, d201909, d201910, d201911, d201912, \
d202001, d202002, d202003, d202004, d202005, d202006, d202007, d202008, d202009, d202010, d202011]
#, d202012 ]

Output2 = pd.concat(Output1)
Output2 = Output2.sort_values(by=["sector", "year", "month"], ascending=True)

Output2['date'] = Output2['month'] + '/' + '1/' + Output2['year']



import pandas

# CDD
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\Japan Weather\Osaka CDD.csv')
table.columns = ['date','CDD', 'Other']
Output2 = pd.merge(Output2, table, how = 'inner', on = "date")
Output2 = Output2.drop(['Other'], axis = 1)

# HDD
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\Japan Weather\Osaka HDD.csv', error_bad_lines=False)
table.columns = ['date','HDD', 'Other']
Output2 = pd.merge(Output2, table, how = 'inner', on = "date")
Output2 = Output2.drop(['Other'], axis = 1)

Output2[["CDD", "HDD"]] = Output2[["CDD", "HDD"]].astype('float')

Output2['com'] = Output2.sector.apply(lambda x: 1 if 'com' in x else 0)
Output2['res'] = Output2.sector.apply(lambda x: 1 if 'res' in x else 0)
Output2['ind'] = Output2.sector.apply(lambda x: 1 if 'ind' in x else 0)

Output2['comHDD'] = Output2.com * Output2.HDD
Output2['resHDD'] = Output2.res * Output2.HDD
Output2['indHDD'] = Output2.ind * Output2.HDD

Output2['comCDD'] = Output2.com * Output2.CDD
Output2['resCDD'] = Output2.res * Output2.CDD
Output2['indCDD'] = Output2.ind * Output2.CDD

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


# Output2.to_csv('C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC 2021\\Weather Seasonality\\Output2.csv',index=None)

#-----------------



file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC 2021\\Weather Seasonality\\MonthDays.xlsx'
sheetName = 'MonthDays'
monthday=pd.read_excel(file_path,sheet_name=sheetName)
Output2 = pd.merge(Output2, monthday, how = 'inner', on = "date")
Output2['valuedaily'] = Output2['value'] / Output2['days']

order = ['sector', 'year', 'month', 'area', 'value', 'date', 'days', 'valuedaily', \
'CDD', 'HDD', 'com', 'res', 'ind', 'comHDD', 'resHDD', 'indHDD', 'comCDD', 'resCDD', 'indCDD']
Output2 = Output2[order]

# highest r2
x = sm.add_constant(Output2.iloc[:,8:]) #生成自变量
y = Output2['valuedaily']
model = sm.OLS(y, x)
result = model.fit()
result.summary()

'''
x = sm.add_constant(Output2.iloc[:,6:11]) #生成自变量
y = Output2['value']
model = sm.OLS(y, x)
result = model.fit()
result.summary()

x = sm.add_constant(Output2.iloc[:,6:110]) #生成自变量
y = Output2['value']
model = sm.OLS(y, x)
result = model.fit()
result.summary()


# output3 is with adjustment, fitted value and fitted deviation
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC 2021\\Weather Seasonality\\Output3.xlsx'
sheetName = 'Target'
table=pd.read_excel(file_path,sheet_name=sheetName)
Output3 = table[6:]
Output3.columns = ['ID', 'sector', 'year', 'month', 'area', 'value', 'date', 'CDD', 'HDD', 'com', 'res', 'ind', \
'value/daily', 'cma', 'hist dev%', 'fitted value', 'fit dev%'] 

Output3[['CDD', 'HDD', 'com', 'res', 'ind', 'value/daily', 'cma', 'hist dev%', 'fitted value', 'fit dev%']] = Output3\
[['CDD', 'HDD', 'com', 'res', 'ind', 'value/daily', 'cma', 'hist dev%', 'fitted value', 'fit dev%']].astype('float')

order = ['ID', 'sector', 'year', 'month', 'area', 'value', 'date', 'value/daily', 'cma', 'hist dev%', 'fitted value', 'fit dev%', \
'CDD', 'HDD', 'com', 'res', 'ind']
Output3 = Output3[order]

Output3['comHDD'] = Output3.com * Output3.HDD
Output3['resHDD'] = Output3.res * Output3.HDD
Output3['indHDD'] = Output3.ind * Output3.HDD

Output3['comCDD'] = Output3.com * Output3.CDD
Output3['resCDD'] = Output3.res * Output3.CDD
Output3['indCDD'] = Output3.ind * Output3.CDD


x = sm.add_constant(Output3.iloc[:,12:]) #生成自变量
y = Output3['value/daily']
model = sm.OLS(y, x)
result = model.fit()
result.summary()

x = sm.add_constant(Output3.iloc[:,12:]) #生成自变量
y = Output3['hist dev%']
model = sm.OLS(y, x)
result = model.fit()
result.summary()

x = sm.add_constant(Output3.iloc[:,12:]) #生成自变量
y = Output3['fitted value']
model = sm.OLS(y, x)
result = model.fit()
result.summary()

# y = deviation %. R2 stays the same, sector ID is insignificant

x = sm.add_constant(Output3.iloc[:,7:12]) #生成自变量
y = Output3['hist dev%']
model = sm.OLS(y, x)
result = model.fit()
result.summary()


x = sm.add_constant(Output3.iloc[:,7:12]) #生成自变量
y = Output3['fit dev%']
model = sm.OLS(y, x)
result = model.fit()
result.summary()

# add cross effect
x = sm.add_constant(Output3.iloc[:,7:12, 18,23]) #生成自变量
y = Output3['value/daily']
model = sm.OLS(y, x)
result = model.fit()
result.summary()



# 画图
# 这两行代码在画图时添加中文必须用
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
model_fit = model.fit(disp=0)

predicts = model.predict() # 模型的预测值
x = datas.iloc[:, 2] # 自变量为第 3 列数据
plt.scatter(x, y, label='实际值') # 散点图
plt.plot(x, predicts, color = 'red', label='预测值')
plt.legend() # 显示图例，即每条线对应 label 中的内容
plt.show() # 显示图形



# -----------------------

Output2.to_csv('C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Summary-By region.csv',index=None)
'''

endtime = datetime.datetime.now()
print ("duration：", endtime - starttime)

print("Congradulations! Finished :)")





