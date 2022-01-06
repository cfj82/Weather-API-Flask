
from flask import Flask, render_template


app = Flask(__name__)



















@app.route('/')  # base.html
def get_weather():
    return test




@app.route('/results')  # results.html
def get_weather():
    return resu














if __name__ == "__main__":
    app.run(debug=True)
