# skibidireze67: Yuhang Pan, Matthew Ciu
# SoftDev 2025
# K29: A RESTful Journey Skyward
# 2025-11-20
# time spent: 1

from flask import Flask, render_template
import json
import urllib.request
import urllib.parse

app = Flask(__name__) 

nasa_key = ymFsQ7dIjWYw0T64b8W4Lyb4IkWcvnc5hXH2IF6k

with urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=" + nasa_key) as response:
    page = response.read()
    # page is in bites, not a dict

dict = json.loads(page.decode('utf-8'))
# use json to convert page from bytes to a usable dict
desc = dict['explanation']
# pulls explanation 
imgurl = dict["hdurl"]

@app.route('/')
def gaming():
    print("newguy") 
    print(dict)
    print("/n gamergod") 
    print(desc)
    print("/n gamergod") 
    print(imgurl)
    return render_template("main.html", desc=desc, imgurl=imgurl)
app.run() 

