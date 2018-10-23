""" Models for dealing with info about types """
import json
import logging

from google.appengine.api import urlfetch

from app.constants import POKEAPI_BASE_DOMAIN
from app.models.types import Type


def get_type(number):
    """ Get a type by number via a pokeapi call """
    type_object = Type.get_by_id(number)
    if type_object:
        logging.info('Found %s, #%s in datastore.', type_object.name, type_object.id_number)
        return type_object.to_json()

    logging.info('Requesting type #%s from pokeapi.', number)
    url = POKEAPI_BASE_DOMAIN.format(u'type/{}'.format(number))
    response = urlfetch.fetch(url, deadline=15)
    response_object = json.loads(response.content)
    type_object = Type(id_number=number, name=response_object.get('name'))
    type_object.key = Type.build_key(number)
    logging.info('Saving %s, #%s to datastore.', type_object.name, type_object.id_number)
    type_object.put()

    return type_object.to_json()
