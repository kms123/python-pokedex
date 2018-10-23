""" Models for storing info about types """
from google.appengine.ext import ndb

from app.models.base import BaseNumberedModel


class Type(BaseNumberedModel):
    """ Information pertaining to a pokemon type """
    @staticmethod
    def build_key(id_number):
        """ Build the key for the entity """
        return ndb.Key(Type, 'TYPE-{}'.format(id_number))
