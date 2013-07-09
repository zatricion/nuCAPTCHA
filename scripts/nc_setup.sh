#!/bin/bash
# git clone https://github.com/zatricion/nuCAPTCHA nucaptcha
# Setup script for nuCAPTCHA

# install necessary packages
sudo apt-get update
sudo apt-get install -q -y python python-software-properties g++ make
sudo apt-get install -q -y python-dev python-virtualenv
sudo apt-get install -q -y mysql-server
sudo apt-get install -q -y libmysqlclient-dev

# create a virtual environment and source it
cd nucaptcha
virtualenv v
source v/bin/activate

# run the setup script
cd wtforms-json-master
python setup.py install

cd ..
pip install -r requirements.txt

# create nucaptcha database
mysql -u root -e "create database nucaptcha"

# set up vim the way I like it, move any existing to old
cd $HOME
if [ -d .vimrc/ ]; then
    mv .vimrc .vimrc_old
fi

cp  ~/nucaptcha/scripts/.vimrc ~/.vimrc

