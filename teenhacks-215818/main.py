#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, jinja2, os
from google.appengine.ext import ndb

template_directory = os.path.join(os.path.dirname(__file__),'templates')
jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(template_directory))

class job(ndb.Model):
    jobTitle = ndb.StringProperty()
    companyName = ndb.StringProperty()
    location = ndb.StringProperty()
    email = ndb.StringProperty()
    pay = ndb.FloatProperty()
    description = ndb.StringProperty()
    tags = ndb.StringProperty(repeated = True)



class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())

class JobsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('jobs.html')
        self.response.out.write(template.render())

class AddJobsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('addJob.html')
        self.response.out.write(template.render())

class EduHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('education.html')
        self.response.out.write(template.render())

class ResourcesHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('resources.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/jobs', JobsHandler),
    ('/addJob', AddJobsHandler),
    ('/edu', EduHandler),
    ('/resources', ResourcesHandler)
], debug=True)
