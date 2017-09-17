import jinja2
import os
import webapp2
from google.appengine.api import images
from google.appengine.ext import ndb
from google.appengine.api import mail
import time

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('main.html')
        self.response.write(template.render())

class Profile(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('profile.html')
        self.response.write(template.render())

class Friends(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('friends.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/profile', Profile),
    ('/friends', Friends),
], debug=True)
