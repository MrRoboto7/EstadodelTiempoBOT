#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, requests, os, json

#twitter information
CONSUMER_KEY = '<Twitter Credentials>'
CONSUMER_SECRET = '<Twitter Credentials>'
ACCESS_KEY = '<Twitter Credentials>'
ACCESS_SECRET = '<Twitter Credentials>'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
response = requests.get('http://api.wunderground.com/api/5ba5077954b9ecff/conditions/lang:SP/q/MX/Morelia.json')
data = response.json()

Twitt = data['current_observation']['weather'] + " Temperatura:" + str(data['current_observation']['temp_c']) + "°C UV:" + str(data['current_observation']['UV']) + " Humedad:" + str(data['current_observation']['relative_humidity']) + " Visibilidad:" + str(data['current_observation']['visibility_km']) + "Km "

precip = float(data['current_observation']['precip_today_metric'])
if precip > 0:
    Twitt = Twitt + "Precipitacion:" + precip + " mm."
else:
    Twitt = Twitt + "Precipitacion: 0%."

#image
url = data['current_observation']['icon_url']
filename = 'temp.jpg'
request = requests.get(url, stream=True)
if request.status_code == 200:
    with open(filename, 'wb') as image:
        for chunk in request:
            image.write(chunk)
    api.update_with_media(filename, status=Twitt)    
    os.remove(filename)
else:
    print("Unable to download image")
time.sleep(1200)#Tweet every 20 minutes
