# https://openweathermap.org/current#current_JSON
import requests as requests
from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')  # base.html
def get_weather():
    return render_template('base.html')


@app.route('/results', methods=["POST"])  # results.html
def show_results():
    city_search = request.form['citycurrent']  # request from base.html input field
    data = get_api_key(city_search)  # call function with ref to city_search
    temp = "{0:.0f}".format(data["list"][0]["main"]["temp"])  # formatted with 2 decimals
    maxt = "{0:.0f}".format(data["list"][0]["main"]["temp_max"])
    mint = "{0:.0f}".format(data["list"][0]["main"]["temp_min"])
    desc = data["list"][0]["weather"][0]["main"]
    location = data["list"][1]["name"]
    return render_template('results.html', temp=temp, maxt=maxt, mint=mint, desc=desc, location=location)


@app.route('/forcast', methods=["POST"])  # forcast.html
def show_forcast_results():
    city_search = request.form['citycurrent']  # request from base.html input field
    data = get_api_forcast(city_search)  # call function with ref to city_search
    location = data["city"]["name"]
    tdesc = data["list"][0]["weather"][0]["description"]
    tmax = data["list"][0]["main"]["temp_max"]
    tmin = data["list"][0]["main"]["temp_min"]

    ttdate = "{:10}".format(data["list"][8]["dt_txt"])  # two days away date
    ttmax = data["list"][8]["main"]["temp_max"]
    ttmin = data["list"][8]["main"]["temp_min"]
    ttdes = data["list"][8]["weather"][0]["description"]

    return render_template('forcast.html', location=location, tmax=tmax, tmin=tmin, tdesc=tdesc, ttdate=ttdate,
                           ttdes=ttdes, ttmax=ttmax, ttmin=ttmin, )


def get_api_key(city_search):
    api_key = '4b998c307c856e851c23f08fdd34f945'
    website = 'http://api.openweathermap.org/data/2.5/find?q='
    # api format:  >> openweathermap.org has wrong api call... use below
    # api.openweathermap.org/data/2.5/find?q=London&units=imperial&appid + api key
    api_call = website + city_search + '&units=imperial&appid=' + api_key
    # call api by request
    response = requests.get(api_call)  # call api from openweather.org
    info = response.json()
    return info


def get_api_forcast(city_search):
    api_key = '4b998c307c856e851c23f08fdd34f945'
    website = 'http://api.openweathermap.org/data/2.5/forecast?q='
    # api format:
    # api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}
    api_forcast_call = website + city_search + '&units=imperial&appid=' + api_key
    response = requests.get(api_forcast_call)  # call api from openweather.org
    info = response.json()
    return info


if __name__ == "__main__":
    app.run(debug=True)
