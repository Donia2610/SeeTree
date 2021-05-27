from flask import Flask, render_template
import requests
from PIL import Image, ImageOps
import numpy as np
from numpy import asarray
import statistics
from statistics import functions 



app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/health")
def health():
    return render_template("OK.html")


@app.route("/stats/<img_name>/<func>")
def stats(img_name,func):
    img_url = "https://storage.googleapis.com/seetree-demo-open/{}".format(img_name)    #create image url
    if not statistics.is_url_image(img_url):
        return render_template("404_img.html")
    
    img = Image.open(requests.get(img_url, stream=True).raw)                            #save as image
    img_gray = ImageOps.grayscale(img)                                                  #convert to grayscale
    img_numpy = asarray(img_gray)                                                       #convert to numpy array
    
    if (func.startswith("p")) and (func[1:].isdigit()) and (int(func[1:]) >= 0 and int(func[1:]) <= 100  ):
        return statistics.find_percentile(img_numpy,img_url,int(func[1:]))

    if not func in functions:
        return render_template("404_func.html")
  
    return functions[func](img_numpy,img_url)                     #call the function that the user chooses 

if __name__=='__main__':
	app.run(host='0.0.0.0', debug=True)
