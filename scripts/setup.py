from models import *
import glob, re

def initialize(image_dir, sec_dir):
    User.create_table(True)
    Image.create_table(True)
    Secondary.create_table(True)
    
    # Add file names to tables
    for file in glob.iglob('{0}*.jpeg'.format(image_dir)):
        Image.create(filename=file, answer=re.sub('jpeg','txt', file))

    for file in glob.iglob('{0}*.jpg'.format(sec_dir)):
        Secondary.create(filename=file)
