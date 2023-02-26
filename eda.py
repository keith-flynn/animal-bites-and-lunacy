import pandas as pd

df = pd.read_csv("assets/Health_AnimalBites.csv")
# These dates need to be the proper Dtypes
print(df.info())
print(df.head())
print(df.describe())

breed_total = df["BreedIDDesc"].value_counts()
print(breed_total)

unique_species = df['SpeciesIDDesc'].unique()
print(unique_species)
print(len(unique_species))

breed_total.to_csv('assets/breed_total.csv')

#df.query['BreedIDDesc ']
