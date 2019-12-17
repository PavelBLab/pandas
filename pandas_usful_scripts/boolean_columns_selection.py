import pandas as pd
import numpy as np

df = pd.read_csv("nhanes_2015_2016.csv")
keep = [column for column in df.columns if 'BM' in column]


index_bool = np.isin(df.columns, keep)
print(index_bool)

# works both with .iloc and .loc
print(df.iloc[:, index_bool])
print(df.loc[:, index_bool])
# print([False, False, True] +[False]*4)
