""" Base API handlers """
import logging

import webapp2

from app.constants import API_USER_KEY_ASSOCIATIONS


class BaseHandler(webapp2.RequestHandler):
    """ Base class for apis """
    def get(self):
        """ get """
        raise NotImplementedError()

    def set_headers(self):
        """ Set standard headers """
        self.response.headers['Content-Type'] = 'application/json'

    def validate_arg_id_number(self):
        """ Validate that the id number passed in is valid """
        number_string = self.request.get('number')
        if not number_string:
            self.abort(400, 'number is required')
        try:
            number = int(number_string)
        except ValueError:
            number = None
            self.abort(400, 'number must be an integer')

        return number

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
