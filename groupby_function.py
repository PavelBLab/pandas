import numpy as np


for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    print('Counties in state ' + group + ' have an average population of ' + str(avg))

# print(df)
import numpy as np
# Your code here
for group, column in df.groupby('Category'):
  # print(group, column)
  totalCategory = np.sum(column['Quantity'] * column['Weight (oz.)'])
  print(group, totalCategory)



print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))

'Or alternatively without using a lambda:'
def totalweight(df, w, q):
       return sum(df[w] * df[q])

print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))
