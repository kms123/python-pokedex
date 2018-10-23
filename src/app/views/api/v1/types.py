import logging

from app.domain.types import get_type
from app.views.api.v1.base import BaseHandler


class GetTypeByNumberHandler(BaseHandler):
    """ Get a type's info by number """
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
        logging.info('Requesting type #%s', number_string)
        response = get_type(number)
        self.response.write(response)
