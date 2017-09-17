import jinja2
import os
import webapp2
from google.appengine.api import images
from google.appengine.ext import ndb
from google.appengine.api import mail
import time

env=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
env1=jinja2.Environment(loader=jinja2.FileSystemLoader(''))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('main.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
