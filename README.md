# Global Weather Analysis

## Background
"What's the weather like as we approach the equator?" Now, we know what you may be thinking: _"Duh. It gets hotter..."_
But, if pressed, how would you **prove** it?

## WeatherPy
I created a Python script to visualize the weather of 500+ cities across the world of varying distance from the equator. To accomplish this, I utilized a [simple Python library](https://pypi.python.org/pypi/citipy), the [OpenWeatherMap API](https://openweathermap.org/api), and a little common sense to create a representative model of weather across world cities.

<img src="output_data/api_pull.png">

Here are a few series of scatter plots to showcase the following relationships:

#### Temperature (F) vs. Latitude
<img src="output_data/Fig1.png">

#### Humidity (%) vs. Latitude
<img src="output_data/Fig2.png">

#### Cloudiness (%) vs. Latitude
<img src="output_data/Fig3.png">

#### Wind Speed (mph) vs. Latitude
<img src="output_data/Fig4.png">



Next I ran linear regression on each relationship, only this time separating them into Northern Hemisphere (greater than or equal to 0 degrees latitude) and Southern Hemisphere (less than 0 degrees latitude):

#### Northern Hemisphere - Temperature (F) vs. Latitude
<img src="output_data/temp_north.png">

####  Southern Hemisphere - Temperature (F) vs. Latitude
<img src="output_data/temp_south.png">

####  Northern Hemisphere - Humidity (%) vs. Latitude
<img src="output_data/humid_north.png">

####  Southern Hemisphere - Humidity (%) vs. Latitude
<img src="output_data/humid_south.png">

####  Northern Hemisphere - Cloudiness (%) vs. Latitude
<img src="output_data/cloud_north.png">

####  Southern Hemisphere - Cloudiness (%) vs. Latitude
<img src="output_data/cloud_south.png">

####  Northern Hemisphere - Wind Speed (mph) vs. Latitude
<img src="output_data/wind_north.png">

####  Southern Hemisphere - Wind Speed (mph) vs. Latitude
<img src="output_data/wind_south.png">


### Conclusion
1) As expected, the weather becomes significantly warmer as one approaches the equator (0 Deg. Latitude). More interestingly, however, is the fact that the southern hemisphere tends to be warmer this time of year than the northern hemisphere. This may be due to the tilt of the earth.
2) There is no strong relationship between latitude and cloudiness. However, it is interesting to see that a strong band of cities sits at 0, 80, and 100% cloudiness.
3) There is no strong relationship between latitude and wind speed. However, in northern hemispheres there is a flurry of cities with over 20 mph of wind.



## VacationPy
Now I used the skills in working with weather data to plan future vacations. I used jupyter-gmaps and the Google Places API for this part of the analysis.

### Heat map that displays the humidity for every city from the WeatherPy
<img src="output_data/humidity_heatmap.png">

I then narrowed down the DataFrame to find my ideal weather conditions:
- A max temperature lower than 80 degrees but higher than 70.
- Wind speed less than 10 mph.
- Zero cloudiness.
- Dropped any rows that don't contain all three conditions. I wanted to be sure the weather is ideal.
<img src="output_data/ideal_weather.png">


Used Google Places API to find the first hotel for each city located within 5000 meters of your coordinates.
<img src="output_data/hotel_dataframe.png">

### Humidity heatmap overlayed with pins containing the **Hotel Name**, **City**, and **Country**.
<img src="output_data/hotel_heatmap.png">
