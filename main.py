from Factory.IndividualFactory import IndividualFactory
from Service.MonteCarloStepService import MonteCarloStepService
from Service.SimulationService import SimulationService
from matplotlib import pyplot as plt
import random as rnd
import datetime
import json
from flask import Flask, request
from flask_restful import reqparse, Resource, Api


app = Flask(__name__)
api = Api(app)

dataList = []

number_of_defective_genes = []
number_of_individs_in_age = []

parser = reqparse.RequestParser()

class SimData(Resource):
    def post(self):
        try:
            json_data = request.get_json()
            t = json_data['t']
            number_of_individs = json_data['number_of_individs']
            number_of_genes = json_data['number_of_genes']
            simulation = SimulationService(number_of_genes, number_of_individs, t)
            simulationData = simulation.Simulate()

            number_of_defective_genes.append(simulationData[0])
            number_of_defective_genes.append(list(range(0, 131)))

            number_of_individs_in_age.append(simulationData[1])
            number_of_individs_in_age.append(list(range(0, 131)))
            return {'number_of_defective_genes': number_of_defective_genes, 'number_of_individs_in_age': number_of_individs_in_age}, 200
        except ValueError:
            print(ValueError)
            return {'message': 'Internal server error'}, 500


class DefectiveGenesEndpoint(Resource):
    def get(self):
        return {'simulation': number_of_defective_genes}


class IndividsInAgeEndpoint(Resource):
    def get(self):
        return {'simulation': number_of_individs_in_age}


api.add_resource(DefectiveGenesEndpoint, '/genes')
api.add_resource(IndividsInAgeEndpoint, '/individuals')
api.add_resource(SimData, '/simdata')

if __name__ == '__main__':
    app.run(debug=True)
