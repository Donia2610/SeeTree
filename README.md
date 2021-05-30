# Junior SW engineer task 🌲
______________________________

Implementation of web server that handles calculation of image statistics. given an image you can calculate:
- Min value 
- Max value
- Mean value
- Median value
- Percentile 

## Setup
Clone the repo and install dependencies
```sh
git clone https://github.com/Donia2610/SeeTree.git
```

## Run using flask
Navigate to 'SeeTree' folder and run the commands below:
```sh
py -m pip install -r requirements.txt
set FLASK_APP=seetree.py
flask run
```
Open http://localhost:5000 on your browser

## Run using Docker
Navigate to 'SeeTree' folder and create Docker image:
```sh
docker build -t seetree .
```
Start the container:
```sh
docker run -d -p 5000:5000 seetree
```
Open http://localhost:5000 on your browser

## Usage 
 The web server will support the following routes:
- /health : will respond with “OK” to any request
- /stats/IMAGE_FILE_NAME/FUNC_NAME : will calculate FUNC_NAME on the pixels of given IMAGE_FILE_NAME and return the result. 
Supported FUNC_NAMES should be:<br>
i. min <br>
ii. max <br>
iii. mean <br>
iv. median <br>
v. pXXX where XXX is a percentile between 0...100. For example p10 is the 10th percentile of the image, p99 is the 99th percentile

## OR
Click on 'Images', browse the images and pick one, then choose the function you wish to know.

## Error handling 
The server responds with error code 404 if an image does not exist or the function is not supported

## Examples
a. Request to /stats/IMG_1.jpg/min should respond with the correct min value in the image <br>
b. Request to /stats/IMG_1.jpg/average should respond with 404 error code <br>
c. Request to /stats/IMG_100.jpg/min should respond with 404 error code (assuming such image was not added to the bucket)

## Bonus ✨
I created a dictionary that saves results from previous requests. If an identical request is made, the result is pulled from the dictionary instead of doing the same calculations again.



