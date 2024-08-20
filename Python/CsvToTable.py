# import pandas as pd
# from sqlalchemy import create_engine

# db_username = 'postgres'
# db_password = 'Mudkip'

# db_host = 'localhost'
# db_port = '5432'
# db_name = 'AirBNB.Aus.Bris'

# engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

# #/Users/aharris/Documents/GitHub/Airbnb_Aus_Bris_DataProject/Airbnb Data
# df1 = pd.read_csv('/Users/aharris/Documents/GitHub/Airbnb_Aus_Bris_DataProject/Airbnb Data/listings.csv', low_memory=False)
# df1.to_sql('AirBNB.Aus.Bris', engine, if_exists='replace', index=False)

# df2 = pd.read_csv('/Users/aharris/Documents/GitHub/Airbnb_Aus_Bris_DataProject/Airbnb Data/neighbourhoods.csv', low_memory=False)
# df2.to_sql('AirBNB.Aus.Bris', engine, if_exists='replace', index=False)

# df3 = pd.read_csv('/Users/aharris/Documents/GitHub/Airbnb_Aus_Bris_DataProject/Airbnb Data/reviews.csv', low_memory=False)
# df3.to_sql('AirBNB.Aus.Bris', engine, if_exists='replace', index=False)

# df4 = pd.read_json('/Users/aharris/Documents/GitHub/Airbnb_Aus_Bris_DataProject/Airbnb Data/neighbourhoods.geojson', low_memory=False)
# df4.to_sql('AirBNB.Aus.Bris', engine, if_exists='replace', index=False)

# print("Tables created and data imported successfully!")

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database # type: ignore

db_username = 'postgres'
db_password = 'Mudkip'
db_host = 'localhost'
db_port = '5432'
db_name = 'AirBNB.Aus.Bris'

engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

# Create database if it doesn't exist
if not database_exists(engine.url):
    create_database(engine.url)
    print(f'Database {db_name} created.')
else:
    print(f'Database {db_name} already exists.')

# Load and import data
df1 = pd.read_csv('/Users/aharris/Documents/GitHub/Airbnb_Aus_Bris_DataProject/Airbnb Data/listings.csv', low_memory=False)
df1.to_sql('listings', engine, if_exists='replace', index=False)

df2 = pd.read_csv('/Users/aharris/Documents/GitHub/Airbnb_Aus_Bris_DataProject/Airbnb Data/neighbourhoods.csv', low_memory=False)
df2.to_sql('neighbourhoods', engine, if_exists='replace', index=False)

df3 = pd.read_csv('/Users/aharris/Documents/GitHub/Airbnb_Aus_Bris_DataProject/Airbnb Data/reviews.csv', low_memory=False)
df3.to_sql('reviews', engine, if_exists='replace', index=False)

df4 = pd.read_json('/Users/aharris/Documents/GitHub/Airbnb_Aus_Bris_DataProject/Airbnb Data/neighbourhoods.geojson', low_memory=False)
df4.to_sql('neighbourhoods_geo', engine, if_exists='replace', index=False)

print("Tables created and data imported successfully!")
