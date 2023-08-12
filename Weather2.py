import requests # this moudle for request url api
from  geopy import distance, geocoders # this moudle for user map and distance
from inquirer import Text, prompt # this moudle for use another method input user 
import pyfiglet # this moudle for user theme text 
from simple_chalk import chalk # this moudle for user color text 
from datetime import datetime 

# !Packege you need install : 
# pyfiglet || simple_chalk || requests || geopy || inquirer
# open terminal or cmd and write : 
# In Windows : pip install packege-name | ex: pip install simple_chalk
# In macos : pip3 install packege-name  | ex: pip3 install simple_chalk
#? print text intro programe 'Weather And Distance' in box
print(chalk.bgBlack(pyfiglet.figlet_format(text='Weather And Distance', font='digital')))
#! create class for use function Weather And Distance
class WeatherAndDistance():
    #! create function weather and use moudle datetime and requests for api
    def Weather(self, City_Country):
        #? create list icon for url: https://openweathermap.org/weather-conditions
        Icon_list = {
            # in the day
            '01d': '🌝',
            '02d': '🌤',
            '03d': '⛅',
            '04d': '🌥',
            '09d': '🌧',
            '10d': '🌦',
            '11d': '⛈',
            '13d': '❄',
            '50d': '🌪',
            # in the night 
            '01n': '🌚',
            '02n': '🌤',
            '03n': '⛅',
            '04n': '⛆',
            '09n': '🌧',
            '10n': '🌦',
            '11n': '⛈',
            '13n': '❄',
            '50n': '🌪'
                    }
        # create api access from website 'weather api'
        Api_Key = "db0a9c0b3ee90b056cccb8b539fb4422"
        # write url from site : 'https://openweathermap.org/current'
        Base_url = "https://api.openweathermap.org/data/2.5/weather?"
        url = f'{Base_url}&q={City_Country}&appid={Api_Key}&units=metric'
        information = requests.get(url)
        # this a new method status_code check 'https://www.geeksforgeeks.org/response-status_code-python-requests/'
        if information.status_code != 200 : 
            information = requests.get(url).json()
            return chalk.red(information['message'].title())
        else:
            # extractions details :
            information = requests.get(url).json()
            temp = information['main']['temp']
            feels_like = information['main']['feels_like']
            temp_min = information['main']["temp_min"]
            temp_max = information['main']["temp_max"]
            description = information['weather'][0]["description"]
            icon = Icon_list[information['weather'][0]["icon"]]
            country = information['sys']["country"]
            city = information['name']
            sunrise_time = datetime.utcfromtimestamp(information['sys']['sunrise'] + information['timezone'])
            sunset_time = datetime.utcfromtimestamp(information['sys']['sunset'] + information['timezone'])
            time = datetime.utcfromtimestamp(information['dt'] + information['timezone'])
            # return details
            return f'{chalk.green(pyfiglet.figlet_format(city, font="slant"))}\
            \n{chalk.red(pyfiglet.figlet_format(country, font="digital"))}\
            \n| {icon} {chalk.bgCyan(description.title())}\
            \n|Temperature: {chalk.bgWhite(temp)}°C\
            \n|Feels Like : {chalk.bgWhite(feels_like)}°C\
            \n|Temperature Max / Mini : ↗️ {chalk.bgGreen(temp_max)}°C | ↘️ {chalk.bgYellow(temp_min)}°C\
            \nLocal Time   🕐:  {chalk.bgWhite(time)}\
            \nSunrise Time 🌝 : {chalk.bgYellow(sunrise_time)}\
            \nSunset Time  🌒 : {chalk.bgBlack(sunset_time)}'
    #! create function distance and use moudle geopy for extraction distance between points
    def Distance(self): 
        first_point = prompt(
            [
                Text("City", message=chalk.bgBlack("Please enter of the first city ")),
                Text("Country", message=chalk.bgBlack("Please enter of the first country "))
            ]
            )
        second_point = prompt(
            [
                Text("City", message=chalk.bgBlack("Please enter of the second city ")),
                Text("Country", message=chalk.bgBlack("Please enter of the second country "))
            ]
            ) 
        first_location = f"{first_point['City']}, {first_point['Country']}"
        first_cords = geocoders.Nominatim(user_agent='distance_calculator').geocode(first_location).point
        second_location = f"{second_point['City']}, {second_point['Country']}"
        second_cords = geocoders.Nominatim(user_agent='distance_calculator').geocode(second_location).point
        distance_km = distance.distance(first_cords, second_cords).km
        return f'The Traveled Distance Between {chalk.bgYellow(first_location)} And {chalk.bgYellow(second_location)} Is:  🛣️   {distance_km:.3f} KM\
            \n 👟  Time Walking: {distance_km / 7:.2f}    Hour\
            \n 🚌  Time Bus:     {distance_km / 80:.2f}   Hour\
            \n 🛩️   Time Airplan: {distance_km / 500:.2f}  Hour'

def run():
    while True:
        try:
            
            class_used = WeatherAndDistance()
            user_choice = int(input(chalk.bold(f'__-----_____-----______------\
                                \n1. Check Weather In Country / City\
                                \n2. Distance Comparison\
                                \n3. Weather Comparison\
                                \n4. Exit\
                                \n|Enter Choice Number: '
                                )))
            if  user_choice not in range(1, 5): 
                raise IndexError()
            elif user_choice == 1 :
                city = input(chalk.bgBlack("Please enter city : "))
                print(class_used.Weather(city))
            elif user_choice == 2 :
                print(class_used.Distance())
            elif user_choice == 3 : 
                first_city = input(chalk.bgBlack('Enter name first city: ')).title()
                second_city = input(chalk.bgBlack('Enter name second city: ')).title()
                if first_city != second_city: 
                    check_first = class_used.Weather(first_city)
                    check_second = class_used.Weather(second_city)
                    if check_first == chalk.red('City Not Found') or check_second == chalk.red('City Not Found'):
                        print(chalk.red('Please Check Your Name City'))
                    else:
                        print(chalk.blue(pyfiglet.figlet_format(first_city, font="digital")))
                        print(check_first)
                        print(chalk.blue(pyfiglet.figlet_format(second_city, font="digital")))
                        print(check_second)
                else:
                    print(class_used.Weather(first_city))
            else :
                print(chalk.green(pyfiglet.figlet_format(text='HIKO DZ', font='slant')))
                print(chalk.bgBlack(pyfiglet.figlet_format(text='Version 1.1', font='digital')))
                print(chalk.red(pyfiglet.figlet_format(text='Enjoy Learning With Codezilla', font='digital')))
                break
        except ValueError: 
            print(chalk.red('🛑 Please enter number 🛑'))

        except IndexError:
            print(chalk.red('🛑 Please enter choice in option 🛑'))
        
        except AttributeError:
            print(chalk.red("Please check your country or city"))

run()
