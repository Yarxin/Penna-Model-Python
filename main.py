from Factory.IndividualFactory import IndividualFactory
from Service.MonteCarloStepService import MonteCarloStepService
from matplotlib import pyplot as plt
import random as rnd
import datetime
import json
from flask import Flask, request
from flask_restful import Resource, Api

########################## Sekcja Interaktywna ##########################
# print("Minimalną liczbę fenotypowych defektów powodujących śmierć genetyczną")
# T = int(input())
#
# print("Podaj liczebność populacji")
# number_of_individs = int(input())
#
# print("Podaj liczbę genów pojedyńczego osobnika")
# number_of_genes = int(input())
#
# print("Podaj wiek prokreacji osobników")
# procreation_age = int(input())

### Sex -> 0 == female, 1 == male ###
start_symulacji = datetime.datetime.now()
print("symulacja start: " + str(start_symulacji))


# T = 50 #min number of fenotype defects, couses death
T = 20
number_of_individs = 100
number_of_genes = 1000
procreation_age = 16 #param_R
max_population = 3 * number_of_individs

sredni_wiek_list = []

number_of_defective_genes = []

years = list(range(0, 131))
individs = [0] * 131

number_of_defective_genes.append(years)
number_of_defective_genes.append(individs)
#########################################################################


########################## Sekcja Symulacyjna ##########################
individualFactory = IndividualFactory()

population = individualFactory.CreatePopuation(number_of_genes, number_of_individs, T, procreation_age)
monteCarloStepService = MonteCarloStepService()
i = 0

while i < number_of_genes:
    defectiveGenesCount = 0
    monteCarloStepService.MonteCarloStep(population, procreation_age, T)

    environmental_capacity = 1 - (len(population) / max_population)
    if environmental_capacity <= 0:
        while environmental_capacity <= 0:
            random_individ_index = rnd.randint(0, len(population) - 1)
            bad_individ = population[random_individ_index]
            population.remove(population[random_individ_index])
            environmental_capacity = 1 - (len(population) / max_population)
            print("usunięto osobnika w wieku: " + str(bad_individ.Age))
    sredni_wiek_populacji = 0
    for individual in population:
        sredni_wiek_populacji += individual.Age

        j = 0
        for gene in individual.Chromatine1:
            if gene == 1 and individual.Chromatine2[j]:
                defectiveGenesCount += 1
                j += 1
            else:
                j += 1
            if j >= individual.Age:
                break
        for year, index in enumerate(number_of_defective_genes[0]):
            if individual.Age == year:
                number_of_defective_genes[1][index] += defectiveGenesCount

    sredni_wiek_populacji = sredni_wiek_populacji / len(population)
    sredni_wiek_list.append(sredni_wiek_populacji)
    print("średni wiek populacji to: " + str(round(sredni_wiek_populacji)))

    i += 1
    print("liczebność populacji w iteracji " + str(i) + " to: " + str(len(population)))

number_of_individs_in_age = []

years = list(range(1, 131))
individs = [0] * 130

number_of_individs_in_age.append(years)
number_of_individs_in_age.append(individs)

for individ in population:
    i = 0
    while i < 130:
        if individ.Age == years[i]:
            number_of_individs_in_age[1][i] += 1
        i += 1

max_number_of_def_genes = max(number_of_defective_genes[1])
max_number_in_age = max(number_of_individs_in_age[1])

scaled_defective_genes = []
scaled_number_in_ages = []

# for value in number_of_defective_genes[1]:
#     value = value / max_number_of_def_genes
#     scaled_defective_genes.append(value)
#
#
# for value in number_of_individs_in_age[1]:
#     value = value / max_number_in_age
#     scaled_number_in_ages.append(value)

scaled_defective_genes.reverse()

stop_symulacji = datetime.datetime.now()
print("Symulacja zakończona: " + str(stop_symulacji))
czas_symulacji = stop_symulacji - start_symulacji
print("czas trwania symulacji: " + str(czas_symulacji))

# plt.plot(years, defectiveGenesList, '.')
# plt.plot(number_of_defective_genes[0], scaled_defective_genes, '.', label='liczba defektywnych genów')
# plt.plot(number_of_individs_in_age[0], scaled_number_in_ages, '.', label='liczba osobników')
# plt.grid(color='black')
# plt.legend()
# plt.xlabel("wiek osobników")
# plt.show()

# iteracje = list(range(0, number_of_genes))
# plt.plot(iteracje, sredni_wiek_list, '.')
# plt.grid(color='black')
# plt.xlabel("iteracja")
# plt.ylabel("średni wiek osobników")
# plt.show()

jsonDefectiveGenes = json.dumps(number_of_defective_genes)
jsonIndivisInAge = json.dumps(number_of_individs_in_age)


################################################################
app = Flask(__name__)
api = Api(app)

todos = {}


class DefectiveGenesEndpoint(Resource):
    def get(self):
        return {'simulation': number_of_defective_genes}


class IndividsInAgeEndpoint(Resource):
    def get(self):
        return {'simulation': number_of_individs_in_age}


api.add_resource(DefectiveGenesEndpoint, '/genes')
api.add_resource(IndividsInAgeEndpoint, '/individuals')

if __name__ == '__main__':
    app.run(debug=True)