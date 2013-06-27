from flask.ext.wtf import Form, TextField, TextAreaField,\
                          HiddenField, SubmitField
import wtforms_json
wtforms_json.init()

class NuCaptchaForm(Form):
  image_id = HiddenField()
  sec_id = HiddenField()
  word = TextField("Enter the first word here: ")
  pos = SubmitField("Positive")
  neg = SubmitField("Negative")
  neut = SubmitField("Neutral")
