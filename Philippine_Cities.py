import pandas as pd

cities = pd.read_json('current.city.list.json')

ph_cities = cities[ (cities['country'] == 'PH') & (cities['stations'].notna()) ]

print(ph_cities)