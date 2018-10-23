""" API handlers for dealing with pokemon """
import logging

from app.domain.pokemon import get_pokemon
from app.views.api.v1.base import BaseHandler


class GetPokemonByNumberHandler(BaseHandler):
    """ Get a specific pokemon's info by number """
    def get(self):
        """ get """
        self.check_credentials()
        self.response.headers['Content-Type'] = 'application/json'
        number_string = self.request.get('number')
        if not number_string:
            self.abort(400, 'number is required')
        try:
            number = int(number_string)
        except ValueError:
            number = None
            self.abort(400, 'number must be an integer')
        logging.info('Requesting pokemon #%s', number_string)
        response = get_pokemon(number)
        self.response.write(response)
