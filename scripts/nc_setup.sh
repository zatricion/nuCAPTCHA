#!/bin/bash
# git clone https://github.com/zatricion/nuCAPTCHA nucaptcha
# Setup script for nuCAPTCHA

# install necessary packages
sudo apt-get update
sudo apt-get install -y python python-software-properties g++ make
sudo apt-get install -y python-dev python-virtualenv

# clone the directory as nucaptcha
cd nucaptcha

# create a virtual environment and source it
virtualenv v
source v/bin/activate

# run the setup script
python wtforms-json-master/setup.py install

pip install -r requirements.txt

# set up vim the way I like it, move any existing to old
cd $HOME
if [ -d .vimrc/ ]; then
    mv .vimrc .vimrc_old
fi

cp  ~/nucaptcha/scripts/.vimrc ~/.vimrc

