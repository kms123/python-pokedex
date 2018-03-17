""" Main entry point for the appengine project, specified in app.yaml """
import webapp2

from routes import ROUTES

APP = webapp2.WSGIApplication(ROUTES, debug=True)
