"""
views imports app, auth, and models, but none of these import views
"""
from flask import render_template, json, jsonify, send_file, request
import random

from app import app
from auth import auth
from models import *

DOMAIN =  'localhost:5000/' #'nucaptcha.us'
IM_DOMAIN = 'http://' + DOMAIN
SEC_DOMAIN = 'http://' + DOMAIN

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


# TODO: ADD SECURITY (can just grab images at all domains)
@app.route('/images/<file>')
def serve_image(file):
  filename = 'images/' + file
  return send_file(filename, mimetype='image/jpeg')
  
@app.route('/secondary/<file>')
def serve_secondary(file):
  filename = 'secondary/' + file
  return send_file(filename, mimetype='image/jpeg')
    
### POST request with info on the answer they gave
@app.route('/', methods=["POST"])
def test():
  try:
    req = request.form
    image_ans = req['image_ans']
    image_id = req['image_id']
    sec_ans = req['sec_ans']
    sec_id = req['sec_id']
    truth_file = Image.get(Image.id == image_id)
    with open(truth_file.answer, 'r') as file:
      image_truth = file.readline().strip()
    if image_ans == image_truth:
      sec_update(sec_id, sec_ans)
      return "True"
    return "False"
  except Exception, e:
    return "{0}".format(e)
    
def sec_update(sec_id, sec_ans):
  if sec_ans == "pos":
    q = Secondary.update(pos_count = Secondary.pos_count + 1).where(Secondary.id == sec_id)
  elif sec_ans == "neg":
    q = Secondary.update(neg_count = Secondary.neg_count + 1).where(Secondary.id == sec_id)
  elif sec_ans == "neut":
    q = Secondary.update(neut_count = Secondary.neut_count + 1).where(Secondary.id == sec_id)
  else:
    raise Exception("Incorrect sentiment value.")
  q.execute()

# TODO: (sometimes require both correct)
# TODO: if <correct> : update database
