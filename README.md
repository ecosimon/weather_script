# weather_script
A simple script to retrieve the current weather in my local area. A script that scrapes api data in my local area, creates a file, write to it and save it in my desktop to view. Everytime i click the script, it will iterate over the existing forecast.

# In order to use this script, you must sign up for a free developer account in 'api.wunderground.com'
Once you've finished signing up, you'll now have access to your own API key.

Open the script in an editor and fill in the api_key with your key.

Now i prefer to have my script and path in the Desktop so that's where i pointed my path, you may change it if you wish.

# Depending on where you live or where you want the forecast at:
Browse through the wundground site and find the exact url address, copy and paste it to your editor.
Copy the part after your api-key and replace it in the requests.get(). The existing code in this script is 
relative to the url-address i specified, so if you decide to choose a different location and parameters, 
change the parsed_json indexes like so. 

# Viola! The script should be usable now!
You should be able to grab your local area forecast if you feel lazy to check your phone or even click and type the forecast site!
All you gotta do is click the script and you'll know the forecast!
