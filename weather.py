import requests

city = "Ocala"
url = 'http://api.weatherapi.com/v1/current.json?key=1d09b36639cb44df8ba10759251702&q='+city+'&aqi=no'

response = requests.get(url)

weather_json= response.json()

temp = weather_json.get('current').get('temp_f')

description = weather_json.get('current').get('condition').get('text')

print("Today's temperature in",city,"is:", str(temp),"degrees Fahrenheit and the weather is", str(description).lower())