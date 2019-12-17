import pandas as pd
revenue_KPIs = ['Revenue Q1 PY', 'Revenue Q1 ACT']
revenue = {'amount': [63149, 63436]}


index = ['Total cost Q1 PY with IFRS16',
        'Interconnect costs',
        'Total HR costs',
        'Customer acquisition cost',
        'Litigation, tax and other regulated payments',
        'Media and Marketing',
        'Other']
data = {'amount': [33587, -926, 888, -656, -339, -245, 224]}

df = pd.DataFrame(data,
                  index=index)
print(df)
print('=======================================================')
'!!!!!!!!!! IMPORTANT index should be in [] always'
print(pd.Series(revenue['amount'][0], index=[revenue_KPIs[0]]))
print('=====')
print(df['amount'].append(pd.Series(revenue['amount'][0], index=[revenue_KPIs[0]])))