""" API handlers for dealing with pokemon """
import logging

from app.domain.pokemon import get_pokemon
from app.views.api.v1.base import BaseHandler


class GetPokemonByNumberHandler(BaseHandler):
    """ Get a specific pokemon's info by number """
    def get(self):
        """ get """
        self.check_credentials()
        self.set_headers()
        number = self.validate_arg_id_number()
        logging.info('Requesting pokemon #%s', number)
        response = get_pokemon(number)
        self.response.write(response)
