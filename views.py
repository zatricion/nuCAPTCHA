"""
views imports app, auth, and models, but none of these import views
"""
from flask import render_template, json, jsonify, send_file, request
from forms import NuCaptchaForm
import random

from app import app
from auth import auth
from models import *

DOMAIN =  'localhost:5000/' #'nucaptcha.us'
IM_DOMAIN = 'http://' + DOMAIN
SEC_DOMAIN = 'http://' + DOMAIN

### Helper Functions ###

def update_known():
  pass
#>>> update_query = Tweet.update(is_published=True).where(Tweet.creation_date < today)

#   q = Secondary.update(known = True, ).where(Secondary.pos_count + Secondary.neg_count + Secondary.neut_count 
#      d = dict(pos = self.pos_count, neg = Secondary.neg_count, neut = Secondary.neut_count)
#         truth = max(d, key=lambda x: x[1])
#         total = sum(d.values())
#         if d[truth] > (0.85 * total) and total > 2:
#             self.truth = truth
#             self.known = True

        
def sec_update(sec_id, req_keys):
  """ Updates the secondary table on reception of a correct post. """
  if "pos" in req_keys:
    q = Secondary.update(pos_count = Secondary.pos_count + 1).where(Secondary.id == sec_id)
  elif "neg" in req_keys:
    q = Secondary.update(neg_count = Secondary.neg_count + 1).where(Secondary.id == sec_id)
  elif "neut" in req_keys:
    q = Secondary.update(neut_count = Secondary.neut_count + 1).where(Secondary.id == sec_id)
  else:
    raise Exception("Incorrect sentiment value.")
  q.execute()

def grab_post(req):
  """ Gets a post and validates the answers. """
  sec_okay = 1
  try:
    image_ans = req['word']
    image_id = req['image_id']
    sec_id = req['sec_id']
    truth_file = Image.get(Image.id == image_id)
    with open(truth_file.answer, 'r') as file:
      image_truth = file.readline().strip()
   # s = Secondary.get(Secondary.id == sec_id)
    #if s.known == 1:
    #    if s.
    if (image_ans == image_truth): # and (s.known == 1):
      sec_update(sec_id, req.keys())
      return "True"
    return "False"
  except Exception, e:
    return "{0}".format(e)
    
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

@app.route('/', methods=['GET', 'POST'])
def serve():
  if  request.method == 'GET':
    default = eval(send_captcha().data)
    form = NuCaptchaForm.from_json(default)
    return render_template('captcha.html', form = form, \
                            image = default['image_url'], \
                            secondary = default['sec_url'])
  else:
    update_known()
    req = request.form
    return grab_post(req)
  
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
