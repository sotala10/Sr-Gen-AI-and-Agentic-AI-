

import pandas as pd

df = pd.read_csv('/Users/sotala/Desktop/AVSCODE/O.TEST/Pandas/data.csv', index_col = "Name")
print(df)

print(df.to_string()) 


tall_pokemon = df[df['Height'] >= 2.0]
print("Pokémon with height greater than or equal to 2.0 meters:")
print(tall_pokemon)

heavy_pokemon = df[df['Weight'] > 150]
print("Pokémon with weight greater than 150 kg:")
print(heavy_pokemon)    

legenedary_pokemon = df[df['Legendary'] == 1]
print("Legendary Pokémon:  ")
print(legenedary_pokemon)

water_pokemon = df[(df['Type1'] == 'Water' )| 
                   (df['Type2'] == 'Water')]
print("Water-type Pokémon:  ")
print(water_pokemon)


ff_pokemon = df[(df['Type1'] == 'Fire') & 
                (df['Type2'] == 'Flying')]

print("Fire-type Pokémon:  ")
print(ff_pokemon)