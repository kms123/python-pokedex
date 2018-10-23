import logging

import webapp2

from app.constants import API_USER_KEY_ASSOCIATIONS


class BaseHandler(webapp2.RequestHandler):

    def get(self):
        raise NotImplemented

    def check_credentials(self):
        """ Check that valid credentials were provided on the request """
        api_user = self.request.get('apiUser')
        if not api_user:
            self.abort(400, 'apiUser is required.')
        api_key = self.request.get('apiKey')
        if not api_key:
            self.abort(400, 'apiKey is required.')

        expected_key = API_USER_KEY_ASSOCIATIONS.get(api_user)
        if not expected_key or not expected_key == api_key:
            self.abort(401, 'Invalid apiUser/apiKey combination.')
        logging.info('Valid authentication. Access granted.')
