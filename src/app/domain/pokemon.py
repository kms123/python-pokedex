""" Domain logic for dealing with pokemon """
import json

from google.appengine.api import urlfetch

from app.constants import POKEAPI_BASE_DOMAIN
from app.models.pokemon import Pokemon


def get_pokemon(number):
    """ Get a pokemon via a pokeapi call """
    pokemon = Pokemon.get_by_id(number)
    if pokemon:
        return pokemon.to_json()


    url = POKEAPI_BASE_DOMAIN.format(u'pokemon/{}'.format(number))
    response = urlfetch.fetch(url, deadline=15)
    response_object = json.loads(response.content)
    pokemon = Pokemon(id_number=number, name=response_object.get('name'))
    pokemon.key = Pokemon.build_key(number)
    pokemon.put()

    return pokemon.to_json()
