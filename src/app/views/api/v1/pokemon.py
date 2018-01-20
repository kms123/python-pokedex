import webapp2


class GetPokemonByNumberHandler(webapp2.RequestHandler):
    def get(self):
        response = {
            'message': 'Pokemon repsonse',
        }
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(response)
