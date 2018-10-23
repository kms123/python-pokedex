""" Base models for different scenarios """
import json

from google.appengine.ext import ndb


class BaseNumberedModel(ndb.Model):
    """ Base model for n object accessed by id number """
    # reference https://cloud.google.com/appengine/docs/standard/python/ndb/
    id_number = ndb.IntegerProperty(required=True)
    name = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @staticmethod
    def build_key(id_number):
        """ Build the key for the entity """
        raise NotImplementedError()

    @classmethod
    def get_by_id(cls, id_number):
        """ Get a model by ID number """
        return cls.build_key(id_number).get()

    def to_json(self):
        """ return a json representation of the object """
        model = {
            'name': self.name,
            'id_number': self.id_number,
            'updated': self.updated.strftime('%Y-%m-%d%H:%M:%S'),
        }
        return json.dumps(model)
