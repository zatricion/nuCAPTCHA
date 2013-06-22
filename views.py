"""
views imports app, auth, and models, but none of these import views
"""
from flask import render_template, json, jsonify, send_file
import glob, random

from app import app
from auth import auth
from models import User

DOMAIN = 'localhost:5000' #'nucaptcha.us'
IM_DOMAIN = 'http://' + DOMAIN + '/images/'
IM_COUNT = 2 # TODO: change to database query
SEC_DOMAIN = 'http://' + DOMAIN + '/secondary/'
SEC_COUNT = 10

### GET request for actual captcha

@app.route('/')
def send_captcha():
  image_id = random.randrange(0, IM_COUNT)
  image_url = IM_DOMAIN + str(image_id)
  
  sec_id = random.randrange(0, SEC_COUNT)
  sec_url = SEC_DOMAIN + str(sec_id)

  # Wrap both image and sentence URLs using jsonify.
  # Then serve both URLs in JSON format. 
  return jsonify(image_id=image_id, image_url=image_url,
                 sec_id=sec_id, sec_url = sec_url)


# ADD SECURITY (can just grab images at all domains)
@app.route('/images/<id>')
def serve_image(id):
  filename = 'images/' + id + '.jpeg'
  return send_file(filename, mimetype='image/jpeg')
  
@app.route('/secondary/<id>')
def serve_secondary(id):
  filename = 'secondary/' + id + '.jpeg'
  return send_file(filename, mimetype='image/jpeg')
    
### POST request with info on the answer they gave

# TODO: return a Bool <correct> (sometimes require both correct)
# TODO: if <correct> : update database
