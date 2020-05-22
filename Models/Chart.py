from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


class Chart(Resource):
    def get(self, chart):
        for value in chart[1]:
            if value != None:
                return chart, 200
        return "Invalid data input", 404

