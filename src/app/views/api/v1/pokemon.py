""" API handlers for dealing with pokemon """
import json

import webapp2

from app.constants import API_USER_KEY_ASSOCIATIONS
from app.domain.pokemon import get_pokemon


class GetPokemonByNumberHandler(webapp2.RequestHandler):
    """ Get a specific pokemon's info by number """
    def get(self):
        """ get """
        self.check_credentials()
        # response = {
        #     'message': 'Pokemon repsonse',
        # }
        response = get_pokemon(1)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(response)

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
            self.abort(403, 'Invalid apiUser/apiKey combination.')
