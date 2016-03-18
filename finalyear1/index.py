#!/usr/bin/env python
import os
import logging
import wsgiref.handlers
import re
import httplib
#import socket
#import sys
#from socket import *
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from util.sessions import Session
from google.appengine.ext import db

class User(db.Model):
  name = db.StringProperty()
  ipaddress = db.StringProperty()
  emailaddress = db.StringProperty()
  mobilenumber = db.StringProperty()
  password = db.StringProperty()
  reenterpassword = db.StringProperty()
  """day = db.StringProperty()
  months = db.StringProperty()
  year = db.StringProperty()
  gender = db.StringProperty()
  security = db.StringProperty()
  answer = db.StringProperty() """

def doRender(handler, tname = 'index.htm', values = { }):  
  temp = os.path.join(
      os.path.dirname(__file__),
      'templates/' + tname)
  if not os.path.isfile(temp):
    return False

  newval = dict(values)
  newval['path'] = handler.request.path
  handler.session = Session()
  if 'username' in handler.session:
     newval['username'] = handler.session['username']

  outstr = template.render(temp, newval)
  handler.response.out.write(outstr)
  return True

class LoginHandler(webapp.RequestHandler):

  def get(self):
    doRender(self, 'loginscreen.htm')

  def post(self):
    self.session = Session()
    name = self.request.get('name')
    emailaddress = self.request.get('emailaddress')
    password = self.request.get('password')
    logging.info('Checking emailaddress='+emailaddress+' password='+password)

    self.session.delete_item('username')
    self.session.delete_item('userkey')

    if name == '' or password == '' or emailaddress == '':
      doRender(
          self,
          'loginscreen.htm',
          {'error' : 'Please fill all the Fields'} )
      return

    que = db.Query(User)
    que = que.filter('name = ', name)
    que = que.filter('emailaddress =',emailaddress)
    que = que.filter('password = ',password)

    results = que.fetch(limit=1)

    if len(results) > 0 :
      user = results[0]
      self.session['userkey'] = user.key()
      self.session['username'] = name
      doRender(self,'profile.htm',{ } )

    else :
      doRender(
          self,
          'loginscreen.htm',
          {'error' : 'All Details Need to Match!! '} )
      return
	
class SignupHandler(webapp.RequestHandler):

  def get(self):
    doRender(self,'applyscreen.htm')
  def post(self):
    self.session = Session()
    name = self.request.get('name')
    ipaddress =  self.request.get('ipaddress')
    emailaddress = self.request.get('emailaddress')
    mobilenumber = self.request.get('mobilenumber')
    password = self.request.get('password')
    reenterpassword = self.request.get('reenterpassword')
    """day = self.request.get('day')
    months= self.request.get('months')
    year = self.request.get('year')
    gender = self.request.get('gender')
    security = self.request.get('security')
    answer = self.request.get('answer') """
    logging.info('Adding email address='+emailaddress)
   
    if name == '' or ipaddress =='' or emailaddress == '' or mobilenumber == '' or password == '' or reenterpassword == '' :
  
      doRender( 
	  self,
	  'applyscreen.htm',
	  {'error' : 'Please fill in all fields'} )
      return
   
    if password != reenterpassword :
      doRender(
          self,
          'applyscreen.htm',
     	  {'error' : 'Check the Passwords'} )
      return 

    if len(emailaddress) < 7 :
      doRender(
          self,
          'applyscreen.htm',
          {'error' : 'Incorrect email address format'} )
      return

    que = db.Query(User).filter('emailaddress =',emailaddress)
    results = que.fetch(limit=1)

    if len(results) > 0 :
      doRender(
          self,
	  'applyscreen.htm',
	  {'error' : 'Account Already Exists'} )
      return
      
    newuser = User(name=name, ipaddress=ipaddress, emailaddress=emailaddress, mobilenumber=mobilenumber, password=password, reenterpassword=reenterpassword );

    pkey = newuser.put();
    self.session['username'] = name
    self.session['userkey'] = pkey
    doRender(self,'profile.htm',{ })

class LogoutHandler(webapp.RequestHandler):

  def get(self):
    self.session = Session()
    self.session.delete_item('username')
    self.session.delete_item('userkey')
    doRender(self, 'index.htm')

class AboutHandler(webapp.RequestHandler):

  def get(self):
    if doRender(self,self.request.path) :
      return
    doRender(self,'about.htm')

class ProfileHandler(webapp.RequestHandler):
  def get(self):
    if doRender(self,self.request.path) :
      return
    doRender(self,'profile.htm')
  
  def post(self):
	
    switch = self.request.get('switches')
    operation = self.request.get('operation')
    ip_address = "10.0.0.200"
    http_request =  ""+ip_address + "/?li=" + switch + "&op=" + operation
    conn = httplib.HTTPConnection(http_request)
    conn.request("GET", " ")
    conn.getresponse()
    #self.response.out.write(http_request)
    #Socket Connectivity
    """
    self.session = Session()
    HOST, PORT = "192.168.1.5", 9999
    data = " ".join(sys.argv[1:])

    sock =socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((HOST, PORT))
        sock.sendall(data + "\n")
        received = sock.recv(1024)
    finally:
        sock.close()

    print "Sent:     {}".format(data)
    print "Received: {}".format(received)  """

class MainHandler(webapp.RequestHandler):

  def get(self):
    if doRender(self,self.request.path) :
      return
    doRender(self,'index.htm') 

def main():
  application = webapp.WSGIApplication([
     ('/login', LoginHandler),
     ('/apply', SignupHandler),     
     ('/logout', LogoutHandler),
     ('/about', AboutHandler),
     ('/profile',ProfileHandler),
     ('/.*', MainHandler)],
     debug=True)
  
  wsgiref.handlers.CGIHandler().run(application)
  
if __name__ == '__main__':
  main()
