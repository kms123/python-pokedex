""" Routes for API endpoints """

from webapp2 import Route

ROUTES = [
    Route('/api/v1/pokemon/get', handler='app.views.api.v1.pokemon.GetPokemonByNumberHandler'),
    Route('/api/v1/type/get', handler='app.views.api.v1.types.GetTypeByNumberHandler')
]
