from Factory.IndividualFactory import IndividualFactory
from Service.MonteCarloStepService import MonteCarloStepService
from matplotlib import pyplot as plt
import random as rnd
import datetime


class SimulationService:
    def __init__(self, paramT, numberOfGenes, numberOfIndivids):
        self.paramT = paramT
        self.numberOfGenes = numberOfGenes
        self.numberOfIndivids = numberOfIndivids

    def Simulate(self):
        start_symulacji = datetime.datetime.now()
        number_of_defective_genes = []

        procreationAge = 16
        maxPopulation = 3 * self.numberOfIndivids

        years = list(range(0, 131))
        individs = [0] * 131

        number_of_defective_genes.append(years)
        number_of_defective_genes.append(individs)

        individualFactory = IndividualFactory()

        population = individualFactory.CreatePopuation(self.numberOfGenes, self.numberOfIndivids, self.paramT, procreationAge)
        monteCarloStepService = MonteCarloStepService()
        i = 0

        while i < self.numberOfGenes:
            defectiveGenesCount = 0
            monteCarloStepService.MonteCarloStep(population, procreationAge, self.paramT)

            environmental_capacity = 1 - (len(population) / maxPopulation)
            if environmental_capacity <= 0:
                while environmental_capacity <= 0:
                    random_individ_index = rnd.randint(0, len(population) - 1)
                    bad_individ = population[random_individ_index]
                    population.remove(population[random_individ_index])
                    environmental_capacity = 1 - (len(population) / maxPopulation)
                    print("usunięto osobnika w wieku: " + str(bad_individ.Age))
            for individual in population:
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
            i += 1
            print(i)

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

        for value in number_of_defective_genes[1]:
            value = value / max_number_of_def_genes
            scaled_defective_genes.append(value)

        for value in number_of_individs_in_age[1]:
            value = value / max_number_in_age
            scaled_number_in_ages.append(value)

        scaled_defective_genes.reverse()

        dataList = []
        dataList.append(scaled_defective_genes)
        dataList.append(scaled_number_in_ages)

        stop_symulacji = datetime.datetime.now()
        print("Symulacja zakończona: " + str(stop_symulacji))
        czas_symulacji = stop_symulacji - start_symulacji
        print("czas trwania symulacji: " + str(czas_symulacji))

        plt.plot(number_of_defective_genes[0], scaled_defective_genes, '.', label='liczba defektywnych genów')
        plt.plot(number_of_individs_in_age[0], scaled_number_in_ages, '.', label='liczba osobników')
        plt.grid(color='black')
        plt.legend()
        plt.xlabel("wiek osobników")
        plt.show()

        return dataList
