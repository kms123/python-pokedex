from google.appengine.api import urlfetch


def get_pokemon(number):
    url = u'https://pokeapi.co/api/v2/pokemon/{}'.format(number)
    response = urlfetch.fetch(url, deadline=15)
    return response.content
