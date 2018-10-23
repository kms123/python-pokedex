""" Models for storing the info about a specific pokemon """
from google.appengine.ext import ndb

from app.models.base import BaseNumberedModel


class Pokemon(BaseNumberedModel):
    """ The information pertaining to a specific pokemon """
    @staticmethod
    def build_key(id_number):
        """ Build the key for the entity """
        return ndb.Key(Pokemon, 'POKEMON-{}'.format(id_number))
