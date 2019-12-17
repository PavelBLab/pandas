



X = df.iloc[:,:4] # first ":" is rows, second ":" columns
X = df.iloc[:,:-1] # ":-1" means all column except the last one

'OR'
X = df.drop('target', axis=1) # 'target is last column
y = df.get('target')