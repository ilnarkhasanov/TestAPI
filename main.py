from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import quotes

todos = {
    1: {"task": "Start doing Haskell", "summary": "Do the assignment"}
}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help="Task is required", required=True)
task_post_args.add_argument("summary", type=str, help="Summary is required", required=True)


class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(quotes.ai_quotes), 200
        for quote in quotes.ai_quotes:
            if quote["id"] == id:
                return quote, 200
        return "Quote not found", 404

    def post(self, id):
        quote = {
            "id": int(id),
            "author": "fewfwe",
            "quote": "fewfwefwef"
        }
        return "fewfwe", 201

        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
        for quote in quotes.ai_quotes:
            if (id == quote["id"]):
                return f"Quote with id {id} already exists", 400
        quote = {
            "id": int(id),
            "author": params["author"],
            "quote": params["quote"]
        }
        quotes.ai_quotes.append(quote)
        return quote, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
        for quote in quotes.ai_quotes:
            if (id == quote["id"]):
                quote["author"] = params["author"]
                quote["quote"] = params["quote"]
                return quote, 200

        quote = {
            "id": id,
            "author": params["author"],
            "quote": params["quote"]
        }

        quotes.ai_quotes.append(quote)
        return quote, 201

    def delete(self, id):
        quotes.ai_quotes = [qoute for qoute in quotes.ai_quotes if qoute["id"] != id]
        return f"Quote with id {id} is deleted.", 200


class ToDo(Resource):
    def get(self, todo_id):
        return todos[todo_id]

    def post(self, todo_id):
        args = task_post_args.parse_args()

        if todo_id in todos:
            return "This id is already taken"

        todos[todo_id] = args

        return todos[todo_id]


app = Flask(__name__)
api = Api(app)
api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")
api.add_resource(ToDo, "/to-do/<int:todo_id>")
if __name__ == '__main__':
    app.run(debug=True)
