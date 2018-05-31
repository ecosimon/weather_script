import os
import urllib
import json
import requests

api_key = 'this is my key'

# This script is meant for learning purposes only, the goal here is to request information from weather.com and then saving its response.text 
# to a file that we will create/write and save to our desktop.

# The path to our Desktop, we set this because by default if you write and
save_path = 'C:/Users/your-user-name/desktop/'

# Naming the .txt file
name_of_file = "Right Now Forecast"

# Now we use os.path.join() to combine the path 
file_name = os.path.join(save_path, name_of_file + ".txt")

# Open the file that we just named, r = read, w = write, x = creates new file, a = appends new text, more in API
# Use W to replace existing files that already exist if you want, but if you want to add existing data to the current file, use "a" instead.
# for test purposes we'll be using "w" to delete old existing data.
file = open(file_name, "w+")

r = requests.get('http://api.wunderground.com/api/' + api_key + '/geolookup/conditions/q/NY/Brooklyn.json')

json_string = r.text
parsed_json = json.loads(json_string)
location = parsed_json['current_observation']['display_location']['full']
temp_f = parsed_json['current_observation']['temp_f']
wind_level = parsed_json['current_observation']['wind_string']
wind_speed = parsed_json['current_observation']['wind_mph']
humidty = parsed_json['current_observation']['relative_humidity']
sky = parsed_json['current_observation']['icon']

text = "Location: {0} \nTemperature: {1} \nWind Speed and Feel: {2}, {3} \nHumidty: {4} \nThe sky is.. {5}".format(location, temp_f, wind_speed, wind_level, humidty, sky)
print(text)

file.write(text)

file.close()
