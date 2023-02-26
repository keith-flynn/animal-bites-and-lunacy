import pandas as pd

bites_df = pd.read_csv("assets/Health_AnimalBites.csv")
moon_df = pd.read_csv('assets/moon_illumination_1800-2100.csv')

print(bites_df.info())
print(bites_df.head())
bites_df['bite_date'] = pd.to_datetime(bites_df['bite_date'], errors = 'coerce')
print(bites_df.info())

# Skipping this for now:
# I was trying to drop the time (00:00:00) but converting using pd.todatetime() seems
# to have dropped the time automatically

# print(bites_df.head())
# bites_df['date'] = bites_df['bite_date'].dt.date
# print(bites_df.head())

print(moon_df.info())
moon_df['date'] = pd.to_datetime(moon_df['date'])
print(moon_df.info())
print(moon_df.head())
moon_df['date'] = moon_df['date'].dt.date
print(moon_df.info())
moon_df['date'] = pd.to_datetime(moon_df['date'])
print(moon_df.head())



test_merge = pd.merge(bites_df, moon_df, left_on='bite_date', right_on='date')
print(test_merge)

# https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates
mask = (test_merge['bite_date'] > '2009-10-28') & (test_merge['bite_date'] <= '2017-09-07')
df = test_merge.loc[mask]

"""
 This didn't work
columns_to_drop = ['vaccination_yrs', 'vaccination_date', 'victim_zip', 'AdvIssuedYNDesc', 
                   'quarantine_date', 'DispositionIDDesc', 'head_sent_date', 'release_date', 
                   'Unnamed: 0', 'date']
"""

df = df.drop(['vaccination_yrs', 'vaccination_date', 'victim_zip', 'AdvIssuedYNDesc', 
                'quarantine_date', 'DispositionIDDesc', 'head_sent_date', 'release_date', 
                'Unnamed: 0', 'date'], axis=1)

print(df)

unique_ResultsIDDesc = df['ResultsIDDesc'].unique()
print(unique_ResultsIDDesc)

unique_WhereBittenIDDesc = df['WhereBittenIDDesc'].unique()
print(unique_WhereBittenIDDesc)

df.to_csv('assets/merged_df.csv')