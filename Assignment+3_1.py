
import pandas as pd
import numpy as np
import re

def answer_one():
        energy = pd.read_excel('Energy Indicators.xls')
        energy = (energy
                  .iloc[16:243]
                  .drop(energy.columns[[0,1]], axis=1)
                  .rename(columns = {'Environmental Indicators: Energy': 'Country',
                                     'Unnamed: 3': 'Energy Supply',
                                     'Unnamed: 4': 'Energy Supply per Capita',
                                     'Unnamed: 5': '% Renewable'})
                  .replace(r'^\.\.\..*', np.nan, regex=True)) #\. means '.' and . means match any characters)

        energy['Energy Supply'] = energy['Energy Supply'] * 1000000

        energy['Country'] =(energy['Country']
                            .replace(r'[0-9]+', '', regex=True)
                            .replace(r'(\s\(.+\))', '', regex=True)
                            .replace({"Republic of Korea": "South Korea",
                                     "United States of America": "United States",
                                     "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                                     "China, Hong Kong Special Administrative Region": "Hong Kong"})
                            .map(lambda x: x.strip()))
        energy = energy.set_index('Country')


        #----------------------------------------------------------------------------------------------------------------


        GDP = pd.read_csv('world_bank.csv', skiprows = 4)
        GDP = GDP.rename(columns = {'Country Name': 'Country'}).set_index('Country')
        GDP = GDP.rename({"Korea, Rep.": "South Korea",
                          "Iran, Islamic Rep.": "Iran",
                          "Hong Kong SAR, China": "Hong Kong"})

        #----------------------------------------------------------------------------------------------------------------


        ScimEn = pd.read_excel('scimagojr-3.xlsx')
        ScimEn = ScimEn.set_index('Country')
        #print(ScimEn)


        #----------------------------------------------------------------------------------------------------------------




        mergeDF_1 = pd.merge(energy, GDP, how = 'inner', left_index=True, right_index=True)
        #print(mergeDF_1)
        mergeDF_2 = (pd.merge(mergeDF_1, ScimEn, how = 'inner', left_index=True, right_index=True)
                     .sort_values('Rank', axis=0, ascending=True)
                     .head(15))
        #print(mergeDF_2)



        finalDF = mergeDF_2[['Rank',
                           'Documents',
                           'Citable documents',
                           'Citations',
                           'Self-citations',
                           'Citations per document',
                           'H index', 'Energy Supply',
                           'Energy Supply per Capita',
                           '% Renewable',
                           '2006',
                           '2007',
                           '2008',
                           '2009',
                           '2010',
                           '2011',
                           '2012',
                           '2013',
                           '2014',
                           '2015']]

        return finalDF
answer_one()



# ### Question 2 (6.6%)
#
def answer_two():
        energy = pd.read_excel('Energy Indicators.xls')
        energy = (energy
                  .iloc[16:243]
                  .drop(energy.columns[[0,1]], axis=1)
                  .rename(columns = {'Environmental Indicators: Energy': 'Country',
                                     'Unnamed: 3': 'Energy Supply',
                                     'Unnamed: 4': 'Energy Supply per Capita',
                                     'Unnamed: 5': '% Renewable'})
                  .replace(r'^\.\.\..*', np.nan, regex=True)) #\. means '.' and . means match any characters)

        energy['Country'] =(energy['Country']
                            .replace(r'[0-9]+', '', regex=True)
                            .replace(r'(\s\(.+\))', '', regex=True)
                            .replace({"Republic of Korea": "South Korea",
                                     "United States of America": "United States",
                                     "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                                     "China, Hong Kong Special Administrative Region": "Hong Kong"}))

        energy = energy.set_index('Country')

        #----------------------------------------------------------------------------------------------------------------



        GDP = pd.read_csv('world_bank.csv')
        header = GDP.iloc[3].apply(str).replace(r'(\.0)', '', regex=True)

        GDP = GDP[4:].rename(columns = header).rename(columns = {'Country Name': 'Country'}).set_index('Country')
        GDP = GDP.rename({"Korea, Rep.": "South Korea",
                          "Iran, Islamic Rep.": "Iran",
                          "Hong Kong SAR, China": "Hong Kong"})

        #----------------------------------------------------------------------------------------------------------------

        ScimEn = pd.read_excel('scimagojr-3.xlsx')
        ScimEn = ScimEn.set_index('Country')

        #----------------------------------------------------------------------------------------------------------------

        mergeDF_outer = (energy.merge(GDP, how = 'outer', left_index=True, right_index=True)
                   .merge(ScimEn, how = 'outer', left_index=True, right_index=True)
                   .sort_values('Rank', axis=0, ascending=True))


        mergeDF_inner = (energy.merge(GDP, how = 'right', left_index=True, right_index=True)
                   .merge(ScimEn, how = 'right', left_index=True, right_index=True)
                   .sort_values('Rank', axis=0, ascending=True))

        return (len(mergeDF_outer) - len(mergeDF_inner))
answer_two()


# ## Answer the following questions in the context of only the top 15 countries by Scimagojr Rank (aka the DataFrame returned by `answer_one()`)

# ### Question 3 (6.6%)
# What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
#
# *This function should return a Series named `avgGDP` with 15 countries and their average GDP sorted in descending order.*

# In[6]:

def answer_three():
    Top15 = answer_one()


    years = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    Top15['avgGDP'] = Top15[years].mean(axis = 1)

    return Top15['avgGDP'].sort_values(ascending=False)


answer_three()


# ### Question 4 (6.6%)
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
#
# *This function should return a single number.*

# In[7]:

def answer_four():

    Top15 = answer_one()


    years = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    Top15['avgGDP'] = Top15[years].mean(axis = 1)
    Top15 = Top15.sort_values('avgGDP', ascending=False)


    Top15['diff'] = Top15['2015'] - Top15['2006']

    return Top15['diff'].iloc[5]
answer_four()


# ### Question 5 (6.6%)
# What is the mean `Energy Supply per Capita`?
#
# *This function should return a single number.*

# In[8]:

def answer_five():
    Top15 = answer_one()
    meanEnergySupplyPerCapita = Top15['Energy Supply per Capita'].mean(axis=0)
    return meanEnergySupplyPerCapita
answer_five()


# ### Question 6 (6.6%)
# What country has the maximum % Renewable and what is the percentage?
#
# *This function should return a tuple with the name of the country and the percentage.*

# In[9]:

def answer_six():
    Top15 = answer_one()
    maxPercentRenewableIndex = Top15['% Renewable'].idxmax()
    maxPercentRenewableValue = Top15['% Renewable'].max()

    return (maxPercentRenewableIndex, maxPercentRenewableValue)

answer_six()


# ### Question 7 (6.6%)
# Create a new column that is the ratio of Self-Citations to Total Citations.
# What is the maximum value for this new column, and what country has the highest ratio?
#
# *This function should return a tuple with the name of the country and the ratio.*

# In[10]:

def answer_seven():
    Top15 = answer_one()
    ratio = Top15['Self-citations'] / Top15['Citations']
    return (ratio.idxmax(), ratio.max())
answer_seven()


# ### Question 8 (6.6%)
#
# Create a column that estimates the population using Energy Supply and Energy Supply per capita.
# What is the third most populous country according to this estimate?
#
# *This function should return a single string value.*

# In[11]:

def answer_eight():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    estimation = Top15['PopEst'].nlargest(3).idxmin()
    return estimation
answer_eight()


# ### Question 9 (6.6%)
# Create a column that estimates the number of citable documents per person.
# What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the `.corr()` method, (Pearson's correlation).
#
# *This function should return a single number.*
#
# *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*

# In[12]:

def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    return Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'], method = 'pearson')
answer_nine()


# In[13]:

def plot9():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])


# In[14]:

plot9() # Be sure to comment out plot9() before submitting the assignment!


# ### Question 10 (6.6%)
# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
#
# *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order of rank.*

# In[15]:

def answer_ten():
    Top15 = answer_one()
    medianPercentRenewable = Top15['% Renewable'].median()
    Top15['HighRenew'] = Top15['% Renewable'] > medianPercentRenewable
    Top15['HighRenew'] = (Top15['HighRenew']
                          .replace(True, '1')
                          .replace(False, '0'))

    return Top15[['HighRenew']]
answer_ten()


# ### Question 11 (6.6%)
ContinentDict  = {'China':'Asia', 
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}

def answer_twelve():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15 = Top15.reset_index()
    Top15['Continent'] = Top15['Country'].map(ContinentDict)
    Top15['% Renewable'] = Top15['% Renewable']

    return (Top15
            .groupby(["Continent",pd.cut(Top15['% Renewable'], 5, labels=["bin{}".format(i) for i in range(5)])])['% Renewable']
            .count())
answer_twelve()


# ### Question 13 (6.6%)
# Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.
#
# e.g. 317615384.61538464 -> 317,615,384.61538464
#
# *This function should return a Series `PopEst` whose index is the country name and whose values are the population estimate string.*

# In[18]:

def answer_thirteen():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    return Top15['PopEst'].map(lambda i: '{:,}'.format(i)) #{:,.2f} 2f means that 2 edcimals after comma
answer_thirteen()


# ### Optional
#
# Use the built in function `plot_optional()` to see an example visualization.

# In[19]:

def plot_optional():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter',
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'],
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' 2014 GDP, and the color corresponds to the continent.")


# In[20]:

plot_optional() # Be sure to comment out plot_optional() before submitting the assignment!


# In[ ]:
