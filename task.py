import flask
from flask import Flask, render_template
from flask.helpers import find_package
from numpy.lib.function_base import percentile
import requests
from PIL import Image, ImageOps
import numpy as np
from numpy import asarray


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
    if not is_url_image(img_url):
        return render_template("404_img.html")
    
    img = Image.open(requests.get(img_url, stream=True).raw)                            #save as image
    img_gray = ImageOps.grayscale(img)                                                  #convert to grayscale
    img_numpy = asarray(img_gray)                                                       #convert to numpy array
    
    if func.startswith("p"):
        return find_percentile(img_numpy,img_url,int(func[1:]))

    if not func in functions:
        return render_template("404_func.html")
  
    return functions[func](img_numpy,img_url)                     #call the function that the user chooses 

# function that calculates percentile
def find_percentile(img_numpy,img_url,num):
    percentile= np.percentile(img_numpy, num)
    return render_template("stats.html", img_url=img_url, stat=percentile, result = "The {}th percentile of this image is:".format(num) )

# function that calculates min
def find_min(img_numpy,img_url):
    min = np.min(img_numpy)
    return render_template("stats.html", img_url=img_url, stat=min, result = "The min of this image is:" )

# function that calculates max
def find_max(img_numpy, img_url):
    max = np.max(img_numpy)
    print(max)
    return render_template("stats.html", img_url=img_url, stat=max, result = "The max of this image is:" )

# function that calculates mean
def find_mean(img_numpy, img_url):
    mean = np.mean(img_numpy)
    print(mean)
    return render_template("stats.html", img_url=img_url, stat=mean, result = "The mean of this image is:" )

# function that calculates median
def find_median(img_numpy, img_url):
    median = np.median(img_numpy)
    print(median)
    return render_template("stats.html", img_url=img_url, stat=median, result = "The min of this image is:" )

# created dictionary for functions available 
functions = {
    'min' : find_min,
    'max' : find_max,
    'mean' : find_mean,
    'median' : find_median
}

#function to check if the url is a valid image
def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False

if __name__=='__main__':
	app.run(host='0.0.0.0', debug=True)


