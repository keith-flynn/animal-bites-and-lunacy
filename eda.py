import pandas as pd

df = pd.read_csv("Health_AnimalBites.csv")
# These dates need to be the proper Dtypes
print(df.info())
print(df.head())
print(df.describe())

breed_total = df["BreedIDDesc"].value_counts()
print(breed_total)

#df.query['BreedIDDesc ']
