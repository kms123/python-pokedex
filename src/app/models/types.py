""" Models for storing info about types """
import json

from google.appengine.ext import ndb


class Type(ndb.Model):
    """ Information pertaining to a pokemon type """
    id_number = ndb.IntegerProperty(required=True)
    name = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @staticmethod
    def build_key(id_number):
        """ Build the key for the entity """
        return ndb.Key(Type, 'TYPE-{}'.format(id_number))

    @classmethod
    def get_by_id(cls, id_number):
        """ Get a Type model by pokemon ID number """
        return cls.build_key(id_number).get()

    def to_json(self):
        """ return a json representation of the object """
        type = {
            'name': self.name,
            'id_number': self.id_number,
            'updated': self.updated.strftime('%Y-%m-%d%H:%M:%S'),
        }

        return json.dumps(type)


