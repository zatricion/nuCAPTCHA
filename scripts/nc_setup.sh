#!/bin/bash
# git clone https://github.com/zatricion/nuCAPTCHA nucaptcha
# Setup script for nuCAPTCHA

# install necessary packages
sudo apt-get update
sudo apt-get install -q -y python python-software-properties g++ make
sudo apt-get install -q -y python-dev python-virtualenv build-essential python-pip
sudo apt-get install -q -y mysql-server
sudo apt-get install -q -y libmysqlclient-dev

### install nginx

# deal with gpg key
echo "deb http://nginx.org/packages/ubuntu/ lucid nginx" >> /etc/apt/sources.list.d/nginx-lucid.list
echo "deb-src http://nginx.org/packages/ubuntu/ lucid nginx" >> /etc/apt/sources.list.d/nginx-lucid.list
wget http://nginx.org/keys/nginx_signing.key
sudo apt-key add nginx_signing.key
rm nginx_signing.key

# actual install
sudo apt-get install -q -y nginx

# create a virtual environment and source it
cd nucaptcha
virtualenv env
source env/bin/activate

# install non-pip library
cd wtforms-json-master
python setup.py install

# install pip libraries
cd ..
pip install -r requirements.txt

### configure uwsgi to run as a daemon

# create a new uwsgi user
sudo useradd -c 'uwsgi user,,,' -g nginx -d /nonexistent -s /bin/false uwsgi

# run uwsgi in the background
echo 'description "uWSGI"\nstart on runlevel [2345]\nstop on runlevel [06]\n\nrespawn\n\nexec uwsgi --master --processes 4 --die-on-term --uid uwsgi --gid nginx --socket /tmp/uwsgi.sock --chmod-socket 660 --no-site --vhost --logto /var/log/uwsgi.log' >> /etc/init/uwsgi.conf

# change permissions
USER = 'michael'
sudo usermod -a -G nginx $USER
sudo chown -R $USER:nginx $HOME/nucaptcha
sudo chmod -R g+w $HOME/nucaptcha

# configure nginx
sudo rm /etc/nginx/conf.d/default.conf
mv $HOME/nucaptcha/scripts/nginx.conf /etc/nginx/conf.d/nucaptcha.conf

# create nucaptcha database
mysql -u root -e "create database nucaptcha"

# set up vim the way I like it, move any existing to old
cd $HOME
if [ -d .vimrc/ ]; then
    mv .vimrc .vimrc_old
fi

cp  ~/nucaptcha/scripts/.vimrc ~/.vimrc

### Start website
sudo service uwsgi restart
sudo service nginx restart
