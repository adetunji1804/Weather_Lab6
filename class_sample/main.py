from openweather import *

def main():
    check = True  
#repeat process while input is wrong         
    while check:
        
        try:#check error
            city_country_extension = get_city_add_extension() #returned city and Abbreviation code stored
            key = os.environ.get('WEATHER_KEY')
            #query = {'q': city_country_extension, 'units': 'imperial', 'appid':'141312562055da1f2e747a4441ac1e17'} #url query created
            query = {'q': city_country_extension, 'units': 'imperial', 'appid':key} #url query created
            url = 'http://api.openweathermap.org/data/2.5/forecast'
            data = requests.get(url, params=query).json() #API data stored in JSON format

            forecast_items = data['list']
            print(f'\nTHE WEATHER FORECAST FOR {city_country_extension.upper()}\n____________________________________ ')
            for forecast in forecast_items: #iterate through received data
                timestamp = forecast['dt']
                date = datetime.fromtimestamp(timestamp) # Unix timestamp
                temp = forecast['main']['temp']
                #display date and temprature of specified city
                print(f'at {date} temp is {temp}') 
                check = False #terminate process
        except: #guard application by displaying the error caught
            print(f'{city_country_extension} not found!')  
        print('\n')

if __name__ == "__main__":
    main()
