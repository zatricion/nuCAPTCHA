"""
views imports app, auth, and models, but none of these import views
"""
from flask import render_template, json, jsonify, send_file, request
import random

from app import app
from auth import auth
from models import *

DOMAIN = 'localhost:5000/' #'nucaptcha.us'
IM_DOMAIN = 'http://' + DOMAIN
IM_COUNT = 2 # TODO: change to database query
SEC_DOMAIN = 'http://' + DOMAIN
SEC_COUNT = 10

### GET request for actual captcha

@app.route('/')
def send_captcha():
  x = Image.select().order_by(fn.Rand()).limit(1) # pick random image
  image_url = IM_DOMAIN + x[0].filename
  
  y = Secondary.select().order_by(fn.Rand()).limit(1) # pick random secondary
  sec_url = SEC_DOMAIN + y[0].filename

  # Wrap both image and sentence URLs using jsonify.
  # Then serve both URLs in JSON format. 
  return jsonify(image_id=x[0].id, image_url=image_url,
                 sec_id=y[0].id, sec_url = sec_url)


# ADD SECURITY (can just grab images at all domains)
@app.route('/images/<file>')
def serve_image(file):
  filename = 'images/' + file
  return send_file(filename, mimetype='image/jpeg')
  
@app.route('/secondary/<file>')
def serve_secondary(file):
  filename = 'secondary/' + file
  return send_file(filename, mimetype='image/jpeg')
    
### POST request with info on the answer they gave
@app.route("/", methods=["POST"])
def test():
  return request.data
    


# TODO: return a Bool <correct> (sometimes require both correct)
# TODO: if <correct> : update database
