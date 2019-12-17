import time
import pandas as pd
import numpy as np
import datetime
# import pandas.io.data as web # io means input/output
import matplotlib.pyplot as plt
from matplotlib import style # make graph a little nicer
style.use('ggplot')
start_time = time.time()
import warnings
warnings.filterwarnings('ignore')

'''
====================================================================================
Data Analysis with Python and Pandas Tutorial
Part 1-2
====================================================================================
'''
web_stats = {'day': [1,2,3,4,5,6],
             'visitors': [43,53,34,45,64,34],
             'bounce_rate': [65, 72, 62, 64, 54, 66],}

df = pd.DataFrame(web_stats)
print(df)
print(df.head()) # print first 5
print(df.tail()) # print last 5
print(df.tail(2)) # print last 2

'!!!!!Set index and create a NEW dataframe'
print(df.set_index('day'))
df2 = df.set_index('day')
print(df2)
print(df2.head(3))

df.set_index('day', inplace=True) # inplace=True can change current df without creating a copy
print(df.head(3))

print(df['visitors'])
print(df.visitors)

'Choose multiple columns'
print(df[['bounce_rate','visitors']])


# print(df['visitors'].tolist()) #you cannot import to columns into list, therefore use below approach
print(np.array(df[['bounce_rate','visitors']]))

df3 = pd.DataFrame(np.array(df[['bounce_rate','visitors']]))
print(df3)

'''
====================================================================================
Data Analysis with Python and Pandas Tutorial
Part 3 - IO Basics
====================================================================================
'''
df1 = pd.read_csv('ZILLOW-Z77006_ZRISFRR.csv')
print(df1.head())

df1.set_index('Date', inplace=True)
print(df1.head())

'Save df under a different name!'
df1.to_csv('newcsv2.csv')

df2 = pd.read_csv('newcsv2.csv') #index will be from 0 to .....
print(df2.head())
'For making "Date" as an index, do the following parameter "index_col=0"'
df2 = pd.read_csv('newcsv2.csv', index_col=0)
print(df2.head())

'Rename column'
df2.columns = ['Austin_HPI'] # HPI -> house price index
print(df2.head())
df2.to_csv('newcsv3.csv')
'Delete headers'
df2.to_csv('newcsv4.csv', header=False)

'parameter "name" -> name headers row[0] and "index_col" -> makes "Date" as an index'
df4 = pd.read_csv('newcsv4.csv', names=['Date', 'Austin_HPI'], index_col=0)
print(df4.head())

df4.to_html('newcsv4.html')

df5 = pd.read_csv('newcsv4.csv', names=['Date', 'Austin_HPI'])
print(df5.head())
"columns={'Austin_HPI':'77006_HPI'} Austin_HPI is existing column name and is new name of the column"
# df5.rename(columns={'Austin_HPI':'77006_HPI'}, inplace=True) #rename 1 column
df5.rename(columns={'Date':'Jopa','Austin_HPI':'77006_HPI'}, inplace=True) #rename 2 columns
print(df5.head())

'''
====================================================================================
Data Analysis with Python and Pandas Tutorial
Part 4 - Building dataset
====================================================================================
'''
# import quandl #https://www.quandl.com
# api_key = 'Kyzvvj5NVfqvTY3EzC4g'
#
# '''
# SGE / NLDHOUS -> house pricing index Netherlands. Not for free, therefore not working
# FMAC/HPI_AK -> House Price Indices - Alaska
# '''
#
# df1 = quandl.get('FMAC/HPI_AK', authtoken=api_key)
# print(df1.head())
#
# us_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#
# ' This is a list'
# print(us_states)
#
# ' This is a dataframe'
# print(us_states[0])
#
# ' Find a column'
# for i in us_states[0]:
#     print(i)
#     # print(us_states[0][i])
# # print(us_states[0]['Abbr'])
# print(us_states[0]['Abbr']['Abbr'])
#
# for abbr in us_states[0]['Abbr']['Abbr'][1:]: #[1:] from 1 row onwards
#     print('FMAC/HPI_' + str(abbr))

'''
====================================================================================
Data Analysis with Python and Pandas Tutorial
Part 5 - Concatenating and Appending dataframes
====================================================================================
'''

df1 = pd.DataFrame({'HPI': [80,85,88,85],
                    'Int_rate': [2,3,2,2],
                    'US_GDP_Thousands': [50,55,60,55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI': [80,85,88,85],
                    'Int_rate': [2,3,2,2],
                    'US_GDP_Thousands': [50,55,60,55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI': [80,85,88,85],
                    'Int_rate': [2,3,2,2],
                    'Low_tier_HPI': [50,55,60,55]},
                   index=[2001, 2002, 2003, 2004])

concat = pd.concat([df1, df2])
print(concat)
concat = pd.concat([df1, df2, df3])
print(concat)

df4 = df1.append(df2)
print(df4)
df4 = df1.append(df3)
print(df4)

s = pd.Series([80, 2, 50], index=['HPI','Int_rate', 'US_GDP_Thousands'])
df4 = df1.append(s, ignore_index=True)
print(df4)

'''
====================================================================================
Data Analysis with Python and Pandas Tutorial
Part 6 - Joining and Merging Dataframes
====================================================================================
'''
df1 = pd.DataFrame({'HPI': [80,85,88,85],
                    'Int_rate': [2,3,2,2],
                    'US_GDP_Thousands': [50,55,60,55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI': [80,85,88,85],
                    'Int_rate': [2,3,2,2],
                    'US_GDP_Thousands': [50,55,60,55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI': [80,85,88,85],
                    'Unemployment_rate': [7,8,9,6],
                    'Low_tier_HPI': [50,55,60,55]},
                   index=[2001, 2002, 2003, 2004])

# print(pd.merge(df1, df2, on=['HPI','Int_rate']))
df1.set_index('HPI', inplace=True)
print(df1)
df3.set_index('HPI', inplace=True)
print(df3)

'"join" method join dataframe only by indexes'
joined = df1.join(df3)
print(joined)

df4 = pd.DataFrame({'Year': [2001, 2002, 2003, 2004],
                    'HPI': [80,85,88,85],
                    'Int_rate': [2,3,2,2],
                    'US_GDP_Thousands': [50,55,60,55]},)


df5 = pd.DataFrame({'Year': [2001, 2003, 2004, 2005],
                    'HPI': [80,85,88,85],
                    'Unemployment_rate': [7,8,9,6],
                    'Low_tier_HPI': [50,55,60,55]},)

merged = df4.merge(df5, on = 'Year', how='left')
print(merged)
merged = df4.merge(df5, on = 'Year', how='right')
print(merged)
merged = df4.merge(df5, on = 'Year', how='inner') # inner merged rows which only match/coincide by 'on', in our case by year. Another words where keys intercept
print(merged)
merged = df4.merge(df5, on = 'Year', how='outer') # outer merged all of the keys -> in our case 'on' it is "Years"
print(merged)

print(merged[(merged['Year'] >= 2003) & (merged['Year'] <= 2004)]) # Do not forget to add boolean mask in parentases

x = merged.set_index('Year')
# print(x.index[0])
print(x.loc[x.index[0], 'Int_rate'])

'''
the best ways to merge dataframes are 'merge' and 'join'. 'Merge' merges df based on key (it can be any column which exists in both df. 'Join' merges df based on indexes interception)
'''

'''
====================================================================================
Data Analysis with Python and Pandas Tutorial
Part 7 - Pickling
====================================================================================
'''
# import quandl #https://www.quandl.com
# import pickle
#
# start_time = time.time()
# api_key = 'Kyzvvj5NVfqvTY3EzC4g'
#
# '''
# SGE / NLDHOUS -> house pricing index Netherlands. Not for free, therefore not working
# FMAC/HPI_AK -> House Price Indices - Alaska
# '''
#
# def state_list():
#     us_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#     # df1 = quandl.get('FMAC/HPI_AK', authtoken=api_key)
#     # print(df1.head())
#     #
#
#     # ' This is a list'
#     # print(us_states)
#     #
#     # ' This is a dataframe'
#     # print(us_states[0])
#     #
#     # ' Find a column'
#     # for i in us_states[0]:
#     #     print(i)
#     #     # print(us_states[0][i])
#     # # print(us_states[0]['Abbr'])
#     # print(us_states[0]['Abbr']['Abbr'])
#     return us_states[0]['Abbr']['Abbr'][1:]
#
#
# def grab_initial_state_data():
#     states = state_list()
#     df_main = pd.DataFrame()
#
#     for abbr in states: #[1:] from 1 row onwards
#         # print('FMAC/HPI_' + str(abbr))
#         query = 'FMAC/HPI_' + str(abbr)
#         df = quandl.get(query, authtoken=api_key)
#         print(df)
#
#         if df_main.empty:
#             # df_main = df
#             df_main = df.reset_index()
#         else:
#         #     df_main = df_main.join(df, on='Date', how='left',lsuffix='_left', rsuffix='_right') # lsuffix to re-write the original column, or rsuffix
#             df_main = df_main.merge(df.reset_index(), on='Date', how='left')
#
#     # df_main.set_index('Date', inplace=True)
#
#     print(df_main.head())
#     pickle_out = open('us_states.pickle', 'wb') # wb -> write bytes
#     pickle.dump(df_main, pickle_out)
#     pickle_out.close()
#
#
# # grab_initial_state_data()
# pickle_in = open('us_states.pickle', 'rb') # rb -> read bytes
# HPI_data = pickle.load(pickle_in)
# print(HPI_data)
#
# 'Alternative make pickle in 2 lines'
# HPI_data.to_pickle('pickle.pickle')
# HPI_data2 = pd.read_pickle('pickle.pickle')
# print(HPI_data2)
#
#
# end_time = time.time()
# scriptRunDuration = (end_time - start_time)/60 # in minutes # measure the execution time of a Python script
# # print(scriptRunDuration)
# minutes = str(scriptRunDuration).split('.')[0]
# seconds = int(str(scriptRunDuration).split('.')[1]) * 60
# print('Took {} min and {} sec'.format(minutes, str(seconds)[:2]))


'''
====================================================================================
Data Analysis with Python and Pandas Tutorial
Part 8 - Percent Change and Correlation Tables
====================================================================================
'''
#
# import quandl #https://www.quandl.com
# import pickle
# import matplotlib.pyplot as plt
# from matplotlib import style
# # style.use('fivethirtyeight')
# style.use('ggplot')
#
#
# api_key = 'Kyzvvj5NVfqvTY3EzC4g'
#
# '''
# SGE / NLDHOUS -> house pricing index Netherlands. Not for free, therefore not working
# FMAC/HPI_AK -> House Price Indices - Alaska
# '''
#
# def state_list():
#     us_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#     # print(us_states)
#     return us_states[0]['Abbr']['Abbr'][1:]
#
#
# def grab_initial_state_data():
#     states = state_list()
#     df_main = pd.DataFrame()
#
#     df_main = quandl.get('FMAC/HPI', authtoken=api_key)
#     print(df_main)
#     print(df_main.columns)
#
#     for abbr in states:
#         # print(df_main[abbr]/df_main[abbr][0])
#         df_main[abbr] = (df_main[abbr]/df_main[abbr][0] - 1) * 100
#
#
#     # print(df_main.head())
#     pickle_out = open('us_states1.pickle', 'wb') # wb -> write bytes
#     pickle.dump(df_main, pickle_out)
#     pickle_out.close()
#
# def HPI_Benchmark():
#     df = quandl.get('FMAC/HPI', authtoken=api_key)
#     df['United States not seasonaly adjusted'] = (df['United States not seasonaly adjusted']/df['United States not seasonaly adjusted'][0] - 1) * 100
#     return df['United States not seasonaly adjusted']
#
# # grab_initial_state_data()
# HPI_Benchmark()
#
#
# HPI_data = pd.read_pickle('us_states1.pickle')
# # print('I am pickle file', HPI_data)
# # print(HPI_data.columns)
# benchmark = HPI_Benchmark()
# print(benchmark)
# print(HPI_data)
#
#
# # print((HPI_data['WI']/HPI_data['WI'][0] -1)*100)
# # HPI_data['WI2'] = HPI_data['WI'] * 2
# # print(HPI_data[['WI','WI2']])
#
# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1),(0,0))
# HPI_data.plot(ax = ax1)
# benchmark.plot(ax=ax1, color='k',linewidth=10)
# plt.legend().remove()
# plt.show()
#
# HPI_State_Correlation = HPI_data.corr()
# print(HPI_State_Correlation)
# print(HPI_State_Correlation.describe())


end_time = time.time()
scriptRunDuration = (end_time - start_time)/60 # in minutes # measure the execution time of a Python script
# print(scriptRunDuration)
timeString = str(scriptRunDuration).split('.')
minutes = timeString[0]
seconds = int(timeString[1]) * 60
print('Took {} min and {} sec'.format(minutes, str(seconds)[:2]))

'''
====================================================================================
Data Analysis with Python and Pandas Tutorial
Part 9 - Resampling
====================================================================================
'''




















