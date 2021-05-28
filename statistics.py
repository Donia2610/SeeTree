from flask import render_template
import numpy as np
import requests

# function that calculates percentile
def find_percentile(img_numpy,img_url,num):
    percentile= np.percentile(img_numpy, num)
    return render_template("stats.html", img_url=img_url, stat=percentile, result = "The {}th percentile of this image is:".format(num) )

# function that calculates min
def find_min(img_numpy,img_url,img_name):
    min = np.min(img_numpy)
    if not img_name in dict_images:
        dict_images[img_name]={}
    dict_images[img_name]['min'] = min
    return render_template("stats.html", img_url=img_url, stat=min, result = "The min of this image is:" )

# function that calculates max
def find_max(img_numpy, img_url,img_name):
    max = np.max(img_numpy)
    if not img_name in dict_images:
        dict_images[img_name]={}
    dict_images[img_name]['max'] = max
    return render_template("stats.html", img_url=img_url, stat=max, result = "The max of this image is:" )

# function that calculates mean
def find_mean(img_numpy, img_url,img_name):
    mean = np.mean(img_numpy)
    if not img_name in dict_images:
        dict_images[img_name]={}
    dict_images[img_name]['mean'] = mean
    return render_template("stats.html", img_url=img_url, stat=mean, result = "The mean of this image is:" )

# function that calculates median
def find_median(img_numpy, img_url,img_name):
    median = np.median(img_numpy)
    if not img_name in dict_images:
        dict_images[img_name]={}
    dict_images[img_name]['median'] = median
    return render_template("stats.html", img_url=img_url, stat=median, result = "The median of this image is:" )

# created dictionary for functions available 
functions = {
    'min' : find_min,
    'max' : find_max,
    'mean' : find_mean,
    'median' : find_median
}

dict_images = {}

#function to check if the url is a valid image
def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False

