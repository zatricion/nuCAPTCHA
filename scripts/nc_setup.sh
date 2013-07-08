#!/bin/bash
# Setup script for nuCAPTCHA

# install necessary packages
sudo apt-get update
sudo apt-get install -y git-core
sudo apt-get install -y python python-software-properties g++ make
sudo apt-get install -y python-dev python-virtualenv

# clone the directory as nucaptcha
git clone https://github.com/zatricion/nuCAPTCHA nucaptcha
cd nucaptcha

# create a virtual environment and source it
virtualenv v
source v/bin/activate

# run the setup script
python wtforms-json-master/setup.py install

pip install -r requirements.txt

