import pandas as pd

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])


# Your answer here
df['Location'] = df.index
df.set_index(['Location', 'Name'], inplace=True)
#print(df.index)
#print(df)
#df.loc['Store 1', 'Chris']

#Name: 'Kevyn', Item Purchased: 'Kitty Food', Cost: 3.00 Location: 'Store 2'.
df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name = ('Store 2', 'Kevyn')))
print(df)
print(census_df.columns)


def answer_eight():
    #print(census_df['REGION'].unique()
    #filtering = census_df[(census_df['REGION'] <= 2) & (census_df['REGION'] >= 1) & (census_df['CTYNAME'] == 'Washington')]
    filter1 = census_df['REGION'].isin([1,2])
    filter2 = census_df['CTYNAME'].str.startswith('Washington')
    filter3 = (census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014'])
    return census_df[filter1 & filter2 & filter3][['STNAME', 'CTYNAME']].sort_index(ascending=True)
answer_eight()
