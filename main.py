# https://openweathermap.org/current#current_JSON

from flask import Flask, render_template
import json
import requests

app = Flask(__name__)


@app.route('/', methods=["GET"])
def get_weather():
    api_key = '4b998c307c856e851c23f08fdd34f945'
    website = 'http://api.openweathermap.org/data/2.5/find?q='
    # .get from entry
    city_name = city_etr.get()
    # api format:
    # api.openweathermap.org/data/2.5/find?q=London&units=imperial
    api_call = website + city_name + '&units=imperial&appid=' + api_key
    # call api by request
    response = requests.get(api_call)
    info = response.json()
    return info


@app.route('/results', methods=["POST"])
def show_results():
    # json format data
    info = response.json()
    temp_display.config(text=(str(info["list"][0]["main"]["temp"]) + " deg F"))
    maxt_display.config(text=(str(info["list"][0]["main"]["temp_max"]) + " deg F"))
    mint_display.config(text=(str(info["list"][0]["main"]["temp_min"]) + " deg F"))
    description_display.config(text=info["list"][0]["weather"][
        "description"])  # todo fix typeError: list indices must be integers or slices, not str

    # weather_lbl.config(text="Error:"+str(response.status_code))  # print response code if error


if __name__ == "__main__":
    app.run(debug=True)
