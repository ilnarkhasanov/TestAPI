from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import quotes


class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(quotes.ai_quotes), 200
        for quote in quotes.ai_quotes:
            if quote["id"] == id:
                return quote, 200
        return "Quote not found", 404


app = Flask(__name__)
api = Api(app)
api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")
if __name__ == '__main__':
    app.run(debug=True)
