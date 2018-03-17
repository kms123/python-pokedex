""" Models for storing the info about a specific pokemon """
from google.appengine.ext import ndb


class Pokemon(ndb.Model):
    """ The information pertaining to a specific pokemon """
    # reference https://cloud.google.com/appengine/docs/standard/python/ndb/
    id_number = ndb.IntegerProperty(required=True)
    name = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @staticmethod
    def build_key(id_number):
        """ Build the key for the entity """
        return ndb.Key('POKEMON-{}'.format(id_number))

    def get_by_id(self, id_number):
        """ Get a pokemon model by pokemon ID number """
        return self.build_key(id_number).get()
