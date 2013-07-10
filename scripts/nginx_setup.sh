#!/bin/bash
# git clone https://github.com/zatricion/nuCAPTCHA nucaptcha
# Setup script for nuCAPTCHA


# install necessary packages
sudo apt-get update
sudo apt-get install -q -y python python-software-properties g++ nginx make
sudo apt-get install -q -y python-dev python-virtualenv build-essential python-pip

# ensure that mysql install runs without user input
# sudo debconf-set-selections <<< 'mysql-server-5.1 mysql-server/root_password password '
# sudo debconf-set-selections <<< 'mysql-server-5.1 mysql-server/root_password_again password '
# sudo debconf-set-selections <<< 'libmysqlclient-dev mysql-server/root_password password '
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

# don't use uwsgi, but maybe later
# uwsgi -s /tmp/uwsgi.sock -w nucaptcha:application -H /home/ubuntu/nucaptcha/env --chmod-socket=666

# set up nginx 
sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default
sudo cp $HOME/nucaptcha/scripts/default.txt /etc/nginx/sites-available/default
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

sudo service nginx restart
python ~/nucaptcha/nucaptcha.py
