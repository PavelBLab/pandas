import pandas as pd
# help(pd.Series)

animals1 = ['Tiger', 'Bear', 'Moose']
numbers1 = [1,2,3]
animalsPandas1 = pd.Series(animals1)
print(animalsPandas1)
numbersPandas1 = pd.Series(numbers1)
print(numbersPandas1)

animals2 = ['Tiger', 'Bear', 'Moose', None]
numbers2 = [1,2,3,None] # this will be converted to NaN means not a number
animalsPandas2 = pd.Series(animals2)
print(animalsPandas2)
numbersPandas2 = pd.Series(numbers2)
print(numbersPandas2)

'''
Important point is None not is not equal to NaN(not a number).
For numpy it is very important as NaN relates to int/float
'''

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
