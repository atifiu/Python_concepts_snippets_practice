import pandas as pd

worldbank_pop = pd.read_csv('./data/WorldBank_POP.csv')
#print(worldbank_pop.head())

#print(worldbank_pop.loc[worldbank_pop['Country Code'] == 'IND'])
worldbank_pop_india = worldbank_pop.loc[worldbank_pop['Country Code'] == 'IND']
print(worldbank_pop_india.head())
#f = lambda x:x/10000000
#value = worldbank_pop_india.loc[:,'Pop'].apply(lambda x:x/10000000)
#worldbank_pop_india.loc[:,'Pop'] = worldbank_pop_india.loc[:,'Pop'].apply(lambda x:x/10000000)
worldbank_pop_india.is_copy = False
#worldbank_pop_india.loc[:,'Pop'] = value
worldbank_pop_india.loc[:,'Pop'] = worldbank_pop_india.loc[:,'Pop'].apply(lambda x:x/10000000)
print(worldbank_pop_india.head())