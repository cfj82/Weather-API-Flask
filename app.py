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
    city_search = request.form['city']
    data = get_api_key(city_search)
    temp = "{0:.0f}".format(data["list"][0]["main"]["temp"])
    maxt = "{0:.0f}".format(data["list"][0]["main"]["temp_max"])
    mint = "{0:.0f}".format(data["list"][0]["main"]["temp_min"])
    desc = data["list"][0]["weather"][0]["main"]
    location = data["list"][1]["name"]
    return render_template('results.html', temp=temp, maxt=maxt, mint=mint, desc=desc, location=location)


def get_api_key(city_search):
    api_key = '4b998c307c856e851c23f08fdd34f945'
    website = 'http://api.openweathermap.org/data/2.5/find?q='
    # api format:
    # api.openweathermap.org/data/2.5/find?q=London&units=imperial
    api_call = website + city_search + '&units=imperial&appid=' + api_key
    # call api by request
    response = requests.get(api_call)
    info = response.json()
    return info

if __name__ == "__main__":
    app.run()
