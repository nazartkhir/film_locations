"""
This module will generate a map of closest film sets to any location.
User has to provide the year and the coordinates.
"""

import argparse
import haversine

def parse_data():
    parser = argparse.ArgumentParser(description='This program will show you nearest filming locations to your coordinates during a certain year')
    parser.add_argument("year", help="a year that you want to see the locations for")
    parser.add_argument("latitude", help="latitude of your location")
    parser.add_argument("longitute", help="longitude of your location")
    args = parser.parse_args()
