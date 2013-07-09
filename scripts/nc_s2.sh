#!/bin/bash
# git clone https://github.com/zatricion/nuCAPTCHA nucaptcha
# Setup script for nuCAPTCHA

# install necessary packages
sudo apt-get update
sudo apt-get install -q -y python python-software-properties g++ make
sudo apt-get install -q -y python-dev python-virtualenv build-essential python-pip
sudo apt-get install -q -y mysql-server
sudo apt-get install -q -y libmysqlclient-dev

sudo apt-get install -q -y make automake nginx gcc g++ python-setuptools
sudo pip install uwsgi


# create a virtual environment and source it
cd ~/nucaptcha
virtualenv env
source env/bin/activate

# install non-pip library
cd wtforms-json-master
python setup.py install

# install pip libraries
cd ~/nucaptcha
pip install -r requirements.txt

cd ~
sudo mkdir -p /var/www/run
sudo cp -R nucaptcha /var/www/nucaptcha

sudo groupadd nginx
sudo usermod -a -G nginx nginx
sudo chown -R nginx:nginx /var/www/

sudo mkdir -p /var/log/uwsgi
sudo mkdir -p /etc/uwsgi/apps-available
sudo mkdir -p /etc/uwsgi/apps-enabled
sudo cp ~/nucaptcha/scripts/uwsgi.conf /etc/init/uwsgi.conf
sudo cp ~/nucaptcha/scripts/nucaptcha.ini /etc/uwsgi/apps-available/nucaptcha.ini
sudo ln -s /etc/uwsgi/apps-available/nucaptcha.ini /etc/uwsgi/apps-enabled/nucaptcha.ini
sudo cp ~/nucaptcha/scripts/default.conf /etc/nginx/conf.d/default.conf

# create nucaptcha database
mysql -u root -e "create database nucaptcha"

# set up vim the way I like it, move any existing to old
cd $HOME
if [ -d .vimrc/ ]; then
    mv .vimrc .vimrc_old
fi

cp  ~/nucaptcha/scripts/.vimrc ~/.vimrc

### Start website
sudo service nginx start
