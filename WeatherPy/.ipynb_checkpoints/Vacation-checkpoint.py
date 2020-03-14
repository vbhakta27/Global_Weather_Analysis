{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# VacationPy\n",
    "----\n",
    "\n",
    "#### Note\n",
    "* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies and Setup\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import requests\n",
    "import gmaps\n",
    "import os\n",
    "\n",
    "# Import API key\n",
    "from api_keys import g_key\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Store Part I results into DataFrame\n",
    "* Load the csv exported in Part I to a DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>City</th>\n",
       "      <th>Cloudiness</th>\n",
       "      <th>Country</th>\n",
       "      <th>Date</th>\n",
       "      <th>Humidity</th>\n",
       "      <th>Lat</th>\n",
       "      <th>Lng</th>\n",
       "      <th>Max Temp</th>\n",
       "      <th>Wind Speed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Albany</td>\n",
       "      <td>90</td>\n",
       "      <td>US</td>\n",
       "      <td>1583946486</td>\n",
       "      <td>36</td>\n",
       "      <td>42.60</td>\n",
       "      <td>-73.97</td>\n",
       "      <td>45.00</td>\n",
       "      <td>5.82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Ushuaia</td>\n",
       "      <td>90</td>\n",
       "      <td>AR</td>\n",
       "      <td>1583946503</td>\n",
       "      <td>87</td>\n",
       "      <td>-54.80</td>\n",
       "      <td>-68.30</td>\n",
       "      <td>46.40</td>\n",
       "      <td>5.82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Hobart</td>\n",
       "      <td>0</td>\n",
       "      <td>AU</td>\n",
       "      <td>1583946314</td>\n",
       "      <td>82</td>\n",
       "      <td>-42.88</td>\n",
       "      <td>147.33</td>\n",
       "      <td>55.40</td>\n",
       "      <td>1.12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Kaniv</td>\n",
       "      <td>100</td>\n",
       "      <td>UA</td>\n",
       "      <td>1583946362</td>\n",
       "      <td>73</td>\n",
       "      <td>49.75</td>\n",
       "      <td>31.46</td>\n",
       "      <td>49.62</td>\n",
       "      <td>15.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>Raudeberg</td>\n",
       "      <td>75</td>\n",
       "      <td>NO</td>\n",
       "      <td>1583946542</td>\n",
       "      <td>86</td>\n",
       "      <td>61.99</td>\n",
       "      <td>5.14</td>\n",
       "      <td>42.80</td>\n",
       "      <td>18.34</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        City  Cloudiness Country        Date  Humidity    Lat     Lng  \\\n",
       "0     Albany          90      US  1583946486        36  42.60  -73.97   \n",
       "1    Ushuaia          90      AR  1583946503        87 -54.80  -68.30   \n",
       "2     Hobart           0      AU  1583946314        82 -42.88  147.33   \n",
       "3      Kaniv         100      UA  1583946362        73  49.75   31.46   \n",
       "4  Raudeberg          75      NO  1583946542        86  61.99    5.14   \n",
       "\n",
       "   Max Temp  Wind Speed  \n",
       "0     45.00        5.82  \n",
       "1     46.40        5.82  \n",
       "2     55.40        1.12  \n",
       "3     49.62       15.50  \n",
       "4     42.80       18.34  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Store filepath in a variable\n",
    "file_one = \"../output_data/cities.csv\"\n",
    "# Not every CSV requires an encoding, but be aware this can come up\n",
    "weather_df = pd.read_csv(file_one)\n",
    "weather_df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Humidity Heatmap\n",
    "* Configure gmaps.\n",
    "* Use the Lat and Lng as locations and Humidity as the weight.\n",
    "* Add Heatmap layer to map."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Configure gmaps\n",
    "gmaps.configure(api_key=g_key)\n",
    "\n",
    "# Store latitude and longitude in locations\n",
    "locations = weather_df[[\"Lat\", \"Lng\"]]\n",
    "\n",
    "# Store humidity values\n",
    "humidity = weather_df[\"Humidity\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f08e765234034ee9b22c647a09de2f4a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Figure(layout=FigureLayout(height='420px'))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot Heatmap\n",
    "fig = gmaps.figure()\n",
    "\n",
    "# Create heat layer\n",
    "heat_layer = gmaps.heatmap_layer(locations, weights=humidity, \n",
    "                                 dissipating=False, max_intensity=100,\n",
    "                                 point_radius=3)\n",
    "\n",
    "\n",
    "# Add layer\n",
    "fig.add_layer(heat_layer)\n",
    "\n",
    "# Display figure\n",
    "fig"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create new DataFrame fitting weather criteria\n",
    "* Narrow down the cities to fit weather conditions.\n",
    "* Drop any rows will null values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hotel Map\n",
    "* Store into variable named `hotel_df`.\n",
    "* Add a \"Hotel Name\" column to the DataFrame.\n",
    "* Set parameters to search for hotels with 5000 meters.\n",
    "* Hit the Google Places API for each city's coordinates.\n",
    "* Store the first Hotel result into the DataFrame.\n",
    "* Plot markers on top of the heatmap."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# NOTE: Do not change any of the code in this cell\n",
    "\n",
    "# Using the template add the hotel marks to the heatmap\n",
    "info_box_template = \"\"\"\n",
    "<dl>\n",
    "<dt>Name</dt><dd>{Hotel Name}</dd>\n",
    "<dt>City</dt><dd>{City}</dd>\n",
    "<dt>Country</dt><dd>{Country}</dd>\n",
    "</dl>\n",
    "\"\"\"\n",
    "# Store the DataFrame Row\n",
    "# NOTE: be sure to update with your DataFrame name\n",
    "hotel_info = [info_box_template.format(**row) for index, row in narrowed_city_df.iterrows()]\n",
    "locations = hotel_df[[\"Lat\", \"Lng\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add marker layer ontop of heat map\n",
    "\n",
    "\n",
    "# Display Map"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  },
  "latex_envs": {
   "LaTeX_envs_menu_present": true,
   "autoclose": false,
   "autocomplete": true,
   "bibliofile": "biblio.bib",
   "cite_by": "apalike",
   "current_citInitial": 1,
   "eqLabelWithNumbers": true,
   "eqNumInitial": 1,
   "hotkeys": {
    "equation": "Ctrl-E",
    "itemize": "Ctrl-I"
   },
   "labels_anchors": false,
   "latex_user_defs": false,
   "report_style_numbering": false,
   "user_envs_cfg": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
