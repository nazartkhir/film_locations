"""
This module will generate a map of closest film sets to any location.
User has to provide the year, the coordinates and a path to the dataset.
"""

import argparse
import haversine
import pandas as pd
import folium

def main():
    args = parse_data()
    df = pd.read_csv(args.path, delimiter='|')
    top_df = calculate_nearest(df, args)
    generate_map(top_df)

def parse_data():
    parser = argparse.ArgumentParser(description='This program will generate a map of closest film sets to any location during a certain year')
    parser.add_argument("year", help="a year that you want to see the locations for", type=int)
    parser.add_argument("latitude", help="latitude of a location", type=float)
    parser.add_argument("longitude", help="longitude of a location", type=float)
    parser.add_argument("path", help="path to the dataset", type=str)
    args = parser.parse_args()
    return args

def calculate_nearest(df, args):
    df = df[df['year'] == args.year]
    for i, row in df.iterrows():
        distance = haversine.haversine((args.latitude, args.longitude), (row['latitude'], row['longitude']))
        df.loc[i, 'distance'] = distance
    df = df.sort_values('distance')[:10]
    return df

def generate_map(df):
    map = folium.Map()
    fg = folium.FeatureGroup(name="Film locations")
    for _, row in df.iterrows():
        fg.add_child(folium.Marker(location=[row['latitude'], row['longitude']],
                            popup=row['name'],
                            icon=folium.Icon()))
    fg_pp = folium.FeatureGroup(name="Population")
    fg_pp.add_child(folium.GeoJson(data=open('world.json', 'r',
                                            encoding='utf-8-sig').read(),
                                  style_function=lambda x: {'fillColor':
          'blue' if (x['properties']['AREA']) == 57935
      else 'green' if (x['properties']['AREA']) < 57935
      else 'red'}))
    map.add_child(fg)
    map.add_child(fg_pp)
    map.save('film_locations.html')
    

main()