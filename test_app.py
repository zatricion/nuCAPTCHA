import flask

application = flask.Flask(__name__)
#Set application.debug=true to enable tracebacks on Beanstalk log output. 
#Make sure to remove this line before deploying to production.
 
@application.route('/')
def hello_world():
    return "Hello world! %s"
 
if __name__ == '__main__':
    application.run(debug=True)