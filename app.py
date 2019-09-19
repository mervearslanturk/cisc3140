from flask import Flask
from flask import render_template
import urllib
import json


urlobj= urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=gGvg7fhg6jaRYZDJQWJ9XdDuUdpib3KOhOceEoSY')
apodread = urlobj.read()
data = json.loads(apodread.decode('utf-8'))

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html',image_url=data["url"])


if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)
