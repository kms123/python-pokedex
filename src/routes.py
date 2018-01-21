""" Routes for API endpoints """

from webapp2 import Route

ROUTES = [
    Route('/api/v1/pokemon/get', handler='app.views.api.v1.pokemon.GetPokemonByNumberHandler')
]
