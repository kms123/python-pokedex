import json
import logging

from google.appengine.api import urlfetch

from app.constants import POKEAPI_BASE_DOMAIN
from app.models.types import Type


def get_type(number):
    """ Get a type by number via a pokeapi call """
    type = Type.get_by_id(number)
    if type:
        logging.info('Found %s, #%s in datastore.', type.name, type.id_number)
        return type.to_json()

    logging.info('Requesting type #%s from pokeapi.', number)
    url = POKEAPI_BASE_DOMAIN.format(u'type/{}'.format(number))
    response = urlfetch.fetch(url, deadline=15)
    response_object = json.loads(response.content)
    type = Type(id_number=number, name=response_object.get('name'))
    type.key = Type.build_key(number)
    logging.info('Saving %s, #%s to datastore.', type.name, type.id_number)
    type.put()

    return type.to_json()
