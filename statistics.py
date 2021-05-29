from flask import render_template
import numpy as np
import requests

# function that calculates percentile
def find_percentile(img_numpy,img_url,img_name,num):
    return np.percentile(img_numpy, num)


# function that calculates min
def find_min(img_numpy,img_url,img_name):
    return np.min(img_numpy)

    
# function that calculates max
def find_max(img_numpy, img_url,img_name):
    return np.max(img_numpy)


# function that calculates mean
def find_mean(img_numpy, img_url,img_name):
    return np.mean(img_numpy)


# function that calculates median
def find_median(img_numpy, img_url,img_name):
    return np.median(img_numpy)


# created dictionary for functions available 
functions = {
    'min' : find_min,
    'max' : find_max,
    'mean' : find_mean,
    'median' : find_median
}

# dictionary to save images data 

dict_images = {}

#function to check if the url is a valid image
def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False

