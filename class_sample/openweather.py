#reference to relevant module
import requests
import os
from datetime import datetime

''' 
function to get country extension code. 
consume API with list of countries and corresponding codes
'''
def get_country_extension(country):
    #list of countries and code's API url
    url ='https://pkgstore.datahub.io/core/country-list/data_json/data/8c458f2d15d9f2119654b29ede6e45b8/data_json.json'
    data = requests.get(url).json() # fetched data stored in JSON format
    #iterate through list to check if user input(country) is on list
    for i in range(len(data)): 
        value = data[i]['Name']
        if value.lower() == country.lower():
            return data[i]['Code'] #return country code


#function to concantinate the city with Abbreviation code
def get_city_add_extension():
    # prompt user for country 
    country = input('Enter country name: ')
    ext = get_country_extension(country) # user input passed as parameter
    if ext == None:
         #country not found, return user input 
        return f'{country}!'
    else:
        #country found, concantinate city with Abbreviation code and return
        choice_city = input('Your choice city ?: ')
        return f'{choice_city},{ext}' 