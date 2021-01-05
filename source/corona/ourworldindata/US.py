
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 5000)

sb.set_style('darkgrid')

"""
https://ourworldindata.org/coronavirus-source-data
"""

full_data = pd.read_csv(r'/home/gopi/Python_202011/data/corona/ourworldindata/owid-covid-data_20210104.csv')
print(full_data.shape)
print(full_data.head(10))
print(full_data.tail())

type(full_data)
type(full_data.date)
type(full_data.location)

print(full_data.head())
print(full_data.loc[0,'location'])
print(full_data.loc[1,'location'])
print(full_data.loc[1,'new_deaths'])

print(full_data.loc[1,'total_deaths'] / full_data.loc[1,'total_cases'])

# The 'count' row has number of non-NA values in the column
print(full_data.describe())
print(full_data.location.value_counts())
print(full_data.date.value_counts())

US = full_data.loc[full_data.location == 'United States',:]
print(US.shape)
print(US.head())
print(US.loc[(US.total_deaths >= 1000),:].head())
US.loc[:,'date'] = pd.to_datetime(US.date, format='%Y-%m-%d')
US.set_index('date', inplace=True)

print(US.tail())

plt.figure()
US[['new_cases', 'new_deaths']].plot(title='New counts from Corona')

plt.figure()
US[['total_cases', 'total_deaths']].plot(title='Total counts from Corona')

plt.figure()
US[['new_deaths', 'total_deaths']].plot(title='Death counts from Corona')

US.loc[:,'death_rate_percentage'] = (US.total_deaths / US.total_cases) * 100
plt.figure()
US[['death_rate_percentage']].plot(title='Death rate percentage from Corona')

US = full_data.loc[full_data.location == 'United States',:]
China = full_data.loc[full_data.location == 'China',:]

full_data.loc[full_data.location == 'United States', ['date', 'location', 'total_cases', 'total_deaths']].tail(4)
full_data.loc[full_data.location == 'China', ['date', 'location', 'total_cases', 'total_deaths']].tail(3)
full_data.loc[full_data.location == 'India', ['date', 'location', 'total_cases', 'total_deaths']].tail(3)
full_data.loc[full_data.location == 'France', ['date', 'location', 'total_cases', 'total_deaths']].tail(3)
