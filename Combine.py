# results

# Combine China Main City CDD and HDD


import pandas as pd 
import numpy as np
from pandas import DataFrame
import datetime

import pandas

# Beijing
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\BeijingCDD.csv')
BeijingCDD = table.iloc[6:41,0:2]
BeijingCDD.columns = ['date','value']
BeijingCDD.insert(BeijingCDD.shape[1], 'area', 'Beijing')
BeijingCDD.insert(BeijingCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
BeijingCDD = BeijingCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\BeijingHDD.csv')
BeijingHDD = table.iloc[6:41,0:2]
BeijingHDD.columns = ['date','value']
BeijingHDD.insert(BeijingHDD.shape[1], 'area', 'Beijing')
BeijingHDD.insert(BeijingHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
BeijingHDD = BeijingHDD[order]

# Changchun
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\ChangchunCDD.csv')
ChangchunCDD = table.iloc[6:41,0:2]
ChangchunCDD.columns = ['date','value']
ChangchunCDD.insert(ChangchunCDD.shape[1], 'area', 'Changchun')
ChangchunCDD.insert(ChangchunCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
ChangchunCDD = ChangchunCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\ChangchunHDD.csv')
ChangchunHDD = table.iloc[6:41,0:2]
ChangchunHDD.columns = ['date','value']
ChangchunHDD.insert(ChangchunHDD.shape[1], 'area', 'Changchun')
ChangchunHDD.insert(ChangchunHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
ChangchunHDD = ChangchunHDD[order]


# Chengdu
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\ChengduCDD.csv')
ChengduCDD = table.iloc[6:41,0:2]
ChengduCDD.columns = ['date','value']
ChengduCDD.insert(ChengduCDD.shape[1], 'area', 'Chengdu')
ChengduCDD.insert(ChengduCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
ChengduCDD = ChengduCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\ChengduHDD.csv')
ChengduHDD = table.iloc[6:41,0:2]
ChengduHDD.columns = ['date','value']
ChengduHDD.insert(ChengduHDD.shape[1], 'area', 'Chengdu')
ChengduHDD.insert(ChengduHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
ChengduHDD = ChengduHDD[order]

# Guangzhou
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\GuangzhouCDD.csv')
GuangzhouCDD = table.iloc[5:40,0:2]
GuangzhouCDD.columns = ['date','value']
GuangzhouCDD.insert(GuangzhouCDD.shape[1], 'area', 'Guangzhou')
GuangzhouCDD.insert(GuangzhouCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
GuangzhouCDD = GuangzhouCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\GuangzhouHDD.csv')
GuangzhouHDD = table.iloc[5:40,0:2]
GuangzhouHDD.columns = ['date','value']
GuangzhouHDD.insert(GuangzhouHDD.shape[1], 'area', 'Guangzhou')
GuangzhouHDD.insert(GuangzhouHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
GuangzhouHDD = GuangzhouHDD[order]

# Shanghai
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\ShanghaiCDD.csv')
ShanghaiCDD = table.iloc[5:40,0:2]
ShanghaiCDD.columns = ['date','value']
ShanghaiCDD.insert(ShanghaiCDD.shape[1], 'area', 'Shanghai')
ShanghaiCDD.insert(ShanghaiCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
ShanghaiCDD = ShanghaiCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\ShanghaiHDD.csv')
ShanghaiHDD = table.iloc[5:40,0:2]
ShanghaiHDD.columns = ['date','value']
ShanghaiHDD.insert(ShanghaiHDD.shape[1], 'area', 'Shanghai')
ShanghaiHDD.insert(ShanghaiHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
ShanghaiHDD = ShanghaiHDD[order]


# Wuhan
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\WuhanCDD.csv')
WuhanCDD = table.iloc[6:41,0:2]
WuhanCDD.columns = ['date','value']
WuhanCDD.insert(WuhanCDD.shape[1], 'area', 'Wuhan')
WuhanCDD.insert(WuhanCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
WuhanCDD = WuhanCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\WuhanHDD.csv')
WuhanHDD = table.iloc[6:41,0:2]
WuhanHDD.columns = ['date','value']
WuhanHDD.insert(WuhanHDD.shape[1], 'area', 'Wuhan')
WuhanHDD.insert(WuhanHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
WuhanHDD = WuhanHDD[order]


# Wulumuqi
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\WulumuqiCDD.csv')
WulumuqiCDD = table.iloc[5:40,0:2]
WulumuqiCDD.columns = ['date','value']
WulumuqiCDD.insert(WulumuqiCDD.shape[1], 'area', 'Wulumuqi')
WulumuqiCDD.insert(WulumuqiCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
WulumuqiCDD = WulumuqiCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\WulumuqiHDD.csv')
WulumuqiHDD = table.iloc[5:40,0:2]
WulumuqiHDD.columns = ['date','value']
WulumuqiHDD.insert(WulumuqiHDD.shape[1], 'area', 'Wulumuqi')
WulumuqiHDD.insert(WulumuqiHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
WulumuqiHDD = WulumuqiHDD[order]

# Xian
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\XianCDD.csv')
XianCDD = table.iloc[6:41,0:2]
XianCDD.columns = ['date','value']
XianCDD.insert(XianCDD.shape[1], 'area', 'Xian')
XianCDD.insert(XianCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
XianCDD = XianCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\China Weather\XianHDD.csv')
XianHDD = table.iloc[6:41,0:2]
XianHDD.columns = ['date','value']
XianHDD.insert(XianHDD.shape[1], 'area', 'Xian')
XianHDD.insert(XianHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
XianHDD = XianHDD[order]



Output1 = [BeijingCDD, BeijingHDD, ChangchunCDD, ChangchunHDD, ChengduCDD, ChengduHDD, GuangzhouCDD, GuangzhouHDD, \
           ShanghaiCDD, ShanghaiHDD, WuhanCDD, WuhanHDD, WulumuqiCDD, WulumuqiHDD, XianCDD, XianHDD]

Output2 = pd.concat(Output1)
Output2.to_csv('C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC 2021\\Weather Seasonality\\China Degree Days.csv',index=None)


# Combine coefficients & R-squared

import pandas as pd 
import numpy as np
from pandas import DataFrame
import datetime

import pandas

# Gifu
file_path = r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\Results\Gifu Results.xlsx'
sheetName = 'Beijing-Gifu'
table = pd.read_excel(file_path,sheet_name=sheetName)
GifuResults = table.iloc[4:16,19:24]
GifuResults.insert(GifuResults.shape[1], 'area', 'Gifu')
GifuResults.columns = ['x', 'coef', 'std', 'err', 't', 'area']
GifuR2 = ['Gifu', table.iloc[2,24]]

# Hokkaido
file_path = r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\Results\Hokkaido Results.xlsx'
sheetName = 'Beijing-Hokkaido'
table = pd.read_excel(file_path,sheet_name=sheetName)
HokkaidoResults = table.iloc[4:16,19:24]
HokkaidoResults.insert(HokkaidoResults.shape[1], 'area', 'Hokkaido')
HokkaidoResults.columns = ['x', 'coef', 'std', 'err', 't', 'area']
HokkaidoR2 = ['Hokkaido', table.iloc[2,24]]

# Kochi
file_path = r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\Results\Kochi Results.xlsx'
sheetName = 'Beijing-Kochi'
table = pd.read_excel(file_path,sheet_name=sheetName)
KochiResults = table.iloc[4:16,19:24]
KochiResults.insert(KochiResults.shape[1], 'area', 'Kochi')
KochiResults.columns = ['x', 'coef', 'std', 'err', 't', 'area']
KochiR2 = ['Kochi', table.iloc[2,24]]


# Okinawa
file_path = r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\Results\Okinawa Results.xlsx'
sheetName = 'Beijing-Okinawa'
table = pd.read_excel(file_path,sheet_name=sheetName)
OkinawaResults = table.iloc[4:16,19:24]
OkinawaResults.insert(OkinawaResults.shape[1], 'area', 'Okinawa')
OkinawaResults.columns = ['x', 'coef', 'std', 'err', 't', 'area']
OkinawaR2 = ['Okinawa', table.iloc[2,24]]

# Osaka
file_path = r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\Results\Osaka Results.xlsx'
sheetName = 'Beijing-Osaka'
table = pd.read_excel(file_path,sheet_name=sheetName)
OsakaResults = table.iloc[4:16,19:24]
OsakaResults.insert(OsakaResults.shape[1], 'area', 'Osaka')
OsakaResults.columns = ['x', 'coef', 'std', 'err', 't', 'area']
OsakaR2 = ['Osaka', table.iloc[2,24]]

# Tohuku
file_path = r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\Results\Tohuku Results.xlsx'
sheetName = 'Beijing-Tohuku'
table = pd.read_excel(file_path,sheet_name=sheetName)
TohukuResults = table.iloc[4:16,19:24]
TohukuResults.insert(TohukuResults.shape[1], 'area', 'Tohuku')
TohukuResults.columns = ['x', 'coef', 'std', 'err', 't', 'area']
TohukuR2 = ['Tohuku', table.iloc[2,24]]

# Tokyo
file_path = r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality\Results\Tokyo Results.xlsx'
sheetName = 'Beijing-Tokyo'
table = pd.read_excel(file_path,sheet_name=sheetName)
TokyoResults = table.iloc[4:16,19:24]
TokyoResults.insert(TokyoResults.shape[1], 'area', 'Tokyo')
TokyoResults.columns = ['x', 'coef', 'std', 'err', 't', 'area']
TokyoR2 = ['Tokyo', table.iloc[2,24]]


### Combine
Output3 = [GifuResults, HokkaidoResults, KochiResults, OkinawaResults, \
           OsakaResults, TohukuResults, TokyoResults]
Output4 = pd.concat(Output3)
Output4.to_csv('C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC 2021\\Weather Seasonality\\Japan Results Combine.csv',index=None)

Output5 = [GifuR2, HokkaidoR2, KochiR2, OkinawaR2, \
           OsakaR2, TohukuR2, TokyoR2]
Output6 = pd.DataFrame(Output5, columns = ['area', 'value'])
Output6.to_csv('C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC 2021\\Weather Seasonality\\Japan Results Combine - R2.csv',index=None)





