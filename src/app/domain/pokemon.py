""" Domain logic for dealing with pokemon """
import json
import logging

from google.appengine.api import urlfetch

from app.constants import POKEAPI_BASE_DOMAIN
from app.models.pokemon import Pokemon


def get_pokemon(number):
    """ Get a pokemon via a pokeapi call """
    pokemon = Pokemon.get_by_id(number)
    if pokemon:
        logging.info('Found %s, #%s in datastore.', pokemon.name, pokemon.id_number)
        return pokemon.to_json()


    logging.info('Requesting pokemon #%s from pokeapi.', number)
    url = POKEAPI_BASE_DOMAIN.format(u'pokemon/{}'.format(number))
    response = urlfetch.fetch(url, deadline=15)
    response_object = json.loads(response.content)
    pokemon = Pokemon(id_number=number, name=response_object.get('name'))
    pokemon.key = Pokemon.build_key(number)
    logging.info('Saving %s, #%s to datastore.', pokemon.name, pokemon.id_number)
    pokemon.put()

    return pokemon.to_json()
