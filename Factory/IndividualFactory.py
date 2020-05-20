from Models.IndividualModel import Individual
import random
import numpy as np


class IndividualFactory:

    def CreatePopuation(self, number_of_genes, number_of_individs, param_T, procreation_age):
        population = []
        i = 0
        while(i < number_of_individs):
            individual = self.__Create(number_of_genes, param_T, procreation_age)
            population.append(individual)
            i += 1
        return population

    def __Create(self, number_of_genes, param_T, procreation_age):
        individual = Individual()
        individual.Genotype = []
        i = 0
        while i < number_of_genes:
            rnd_1 = random.randint(1, 20) # 5% na powstanie genu defektywnego
            if rnd_1 == 1:
                individual.Chromatine1.append(1)
            else:
                individual.Chromatine1.append(0) # 5% na powstanie genu defektywnego
            rnd_2 = random.randint(1, 20)
            if rnd_2 == 1:
                individual.Chromatine2.append(1)
            else:
                individual.Chromatine2.append(0)
            individual.T = 0
            individual.Procreation_age = procreation_age
            # individual.Age = random.randint(1, number_of_genes)
            individual.Age = random.randint(1, 80)
            individual.Sex = random.randint(0, 1)
            i += 1
        return individual
