#!/bin/bash
# git clone https://github.com/zatricion/nuCAPTCHA nucaptcha
# Setup script for nuCAPTCHA

# ensure that mysql install runs without user input
export DEBIAN_FRONTEND=noninteractive

# install necessary packages
sudo apt-get update
sudo apt-get install -q -y python python-software-properties g++ make
sudo apt-get install -q -y python-dev python-virtualenv build-essential python-pip
sudo apt-get install -q -y mysql-server
sudo apt-get install -q -y libmysqlclient-dev

# create a virtual environment and source it
cd $HOME/nucaptcha
virtualenv env
source env/bin/activate

# install non-pip library
cd wtforms-json-master
python setup.py install

# install pip libraries
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

