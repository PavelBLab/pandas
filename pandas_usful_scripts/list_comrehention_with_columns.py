import pandas as pd
pd.set_option('display.max_columns', 10)



df = pd.read_csv("nhanes_2015_2016.csv")

# One way to get the column names we want to keep is simply by copying from the above output and storing in a list
keep_1 = ['BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC','BMXWAIST']
print(keep_1)

# Another way to get only column names that include 'BMX' is with list comprehension
# [keep x for x in list if condition met]
keep_2 = [column for column in df.columns if 'BM' in column]
print(keep_2)

# use [] notation to keep columns
df_BMX = df[keep_2]
print(df_BMX)



