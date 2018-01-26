""" Models for storing the info about a specific pokemon """
from google.appengine.ext import ndb


class Pokemon(ndb.Model):
    """ The information pertaining to a specific pokemon """
    # reference https://cloud.google.com/appengine/docs/standard/python/ndb/
    id = ndb.IntegerProperty(required=True)
    name = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    def build_key(self, id):
        return 'POKEMON-' + self.id
