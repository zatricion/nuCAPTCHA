"""
views imports app, auth, and models, but none of these import views
"""
from flask import render_template, json, jsonify, send_file, request
from forms import NuCaptchaForm
import random

from app import app
from auth import auth
from models import User, Image, Secondary, fn

DOMAIN =  'nucaptcha.us/'
IM_DOMAIN = 'http://' + DOMAIN
SEC_DOMAIN = 'http://' + DOMAIN

### Helper Functions ###
      
def sec_update(sec_id, sec_ans):
  """ Updates the secondary table on reception of a correct post. """  
  if sec_ans == 'Positive':
    q = Secondary.update(pos_count = Secondary.pos_count + 1).where(Secondary.id == sec_id)
  elif sec_ans == 'Negative':
    q = Secondary.update(neg_count = Secondary.neg_count + 1).where(Secondary.id == sec_id)
  elif sec_ans == 'Neutral':
    q = Secondary.update(neut_count = Secondary.neut_count + 1).where(Secondary.id == sec_id)
  else:
    raise Exception("Incorrect sentiment value.")
  q.execute()

def grab_post(req):
  """ Gets a post and validates the answers. """
  sec_okay = 1
  image_ans = req.get('word', None)
  image_id = req.get('image_id', None)
  sec_id = req.get('sec_id', None)
  sec_ans = req.get('sec_ans', None) 
  
  truth_file = Image.get(Image.id == image_id)
  with open(truth_file.answer, 'r') as file:
    image_truth = file.readline().strip()
 
  s = Secondary.get(Secondary.id == sec_id)
  known = s.known(2, 0.85)
  if ((image_ans == image_truth) and
      (not known or (known and (s.truth['word'] == sec_ans))) ):
    sec_update(sec_id, sec_ans)    
    return True
  else:
    return False
 
def send_captcha():
  """ Picks a random combination of image and sentence. """
  x = Image.select().order_by(fn.Rand()).limit(1) # pick random image
  image_url = IM_DOMAIN + x[0].filename
  
  y = Secondary.select().order_by(fn.Rand()).limit(1) # pick random secondary
  sec_url = SEC_DOMAIN + y[0].filename

  # Wrap both image and sentence URLs using jsonify.
  # Then serve both URLs in JSON format. 
  return jsonify(image_id=x[0].id, image_url=image_url,
                 sec_id=y[0].id, sec_url = sec_url)


### Routing Functions ###

@app.route('/', methods=['GET'])
def serve():
    default = eval(send_captcha().data)
    form = NuCaptchaForm.from_json(default)
    return render_template('captcha.html', form = form,
                            image = default['image_url'],
                            secondary = default['sec_url'])
                            
@app.route('/', methods=['POST'])
def acquire():
    #update_known()
    req = request.form
    return str(grab_post(req))
  
# TODO: ADD SECURITY (can just grab images at all domains)
@app.route('/images/<file>')
def serve_image(file):
  filename = 'images/' + file
  return send_file(filename, mimetype='image/jpeg')
  
@app.route('/secondary/<file>')
def serve_secondary(file):
  filename = 'secondary/' + file
  return send_file(filename, mimetype='image/jpeg')
    

# TODO: (sometimes require both correct)
