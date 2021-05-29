from flask import Flask, render_template
import requests
from PIL import Image, ImageOps
import numpy as np
from numpy import asarray
import statistics
from statistics import functions, dict_images



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
    if img_name in dict_images:                                                         #check if image results are in dictionary
        if func in dict_images[img_name]:
            return render_template("stats.html", img_url=img_url, stat=dict_images[img_name][func], result = "We told you, The {} of this image is:".format(func) ) 

    img = Image.open(requests.get(img_url, stream=True).raw)                            #save as image
    img_gray = ImageOps.grayscale(img)                                                  #convert to grayscale
    img_numpy = asarray(img_gray)                                                       #convert to numpy array
    
    if (func.startswith("p")) and (func[1:].isdigit()) and (int(func[1:]) >= 0 and int(func[1:]) <= 100  ):
        num = int(func[1:])
        if img_name in dict_images:                                                      #check if image results are in dictionary
            if num in dict_images[img_name]:
                return render_template("stats.html", img_url=img_url, stat=dict_images[img_name][num], result = "We told you, The {}th percentile of this image is:".format(num)) 
        res = statistics.find_percentile(img_numpy,img_url,img_name,num)
        if not img_name in dict_images:
            dict_images[img_name]={}
        dict_images[img_name][num] = res
        return render_template("stats.html", img_url=img_url, stat=res, result = "The {}th percentile of this image is:".format(num) )

    if not func in functions:
        return render_template("404_func.html")

    res = functions[func](img_numpy,img_url,img_name)                     #call the function that the user chooses 
    if not img_name in dict_images:
        dict_images[img_name]={}
    dict_images[img_name][func] = res 
    return render_template("stats.html", img_url=img_url, stat=res, result = "The {} of this image is:".format(func) )


@app.route("/stats")                              # displays photos available so that the user can choose from
def display():
    return render_template("display.html")


@app.route("/stats/<img>")                          # after the chooses an image he can choose the function 
def funcs(img):
    return render_template("funcs.html",img=img)




if __name__=='__main__':
	app.run(host='0.0.0.0', debug=True)


