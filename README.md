nuCAPTCHA
================================

Check out https://www.nucaptcha.us.

On an AWS ubuntu instance:
* sudo apt-get install -y git
* git clone https://github.com/zatricion/nuCAPTCHA nucaptcha
* cd nucaptcha
* chmod 777 scripts/nginx_setup.sh
* ./scripts/nginx_setup.sh
* source env/bin/activate
* python nucaptcha.py


Local setup:

Use the local branch.

Install mysql and create a database called nucaptcha.

Feel free to install virtualenv and create and source a virtual environment
before doing these things.
* pip install -r requirements.txt
* cd wtforms-json-master; python setup.py install
* cd ..
* python nucaptcha.py

