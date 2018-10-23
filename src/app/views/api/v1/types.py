""" API handlers for dealing with pokemon """
import logging

from app.domain.types import get_type
from app.views.api.v1.base import BaseHandler


class GetTypeByNumberHandler(BaseHandler):
    """ Get a type's info by number """
    def get(self):
        """ get """
        self.check_credentials()
        self.set_headers()
        number = self.validate_arg_id_number()
        logging.info('Requesting type #%s', number)
        response = get_type(number)
        self.response.write(response)
