# Yuhang Pan
# SoftDev 2026
# Continuous Integration DEMO

from flask import Flask, render_template
import json
import urllib.request
import urllib.parse

app = Flask(__name__)

@app.route('/home')
def gaming():
    with open("key_nasa.txt") as file:
        nasa_key = file.read()

    with urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=" + nasa_key) as response:
        page = response.read()
        # page is in bites, not a dict

    dict = json.loads(page.decode('utf-8'))
    # use json to convert page from bytes to a usable dict
    desc = dict['explanation']
    # pulls explanation
    imgurl = dict["hdurl"]

    print(dict)
    print("/n")
    print(desc)
    print("/n")
    print(imgurl)
    return render_template("main.html", desc=desc, imgurl=imgurl)

if __name__ == "__main__":
    app.run()
